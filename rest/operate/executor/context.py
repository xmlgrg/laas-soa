import json
import logging
import os
import threading

import paramiko

from exception import MyServiceException
from rest.operate.cmdb import data

global_data = threading.local()
"""
上下文环境
"""


def select_data_by_data_id__data_data_id(data_id, data_data_id):
    """
    查询业务数据
    :param data_id:
    :param data_data_id:
    :return:
    """
    return data.select_by_data_id__data_data_id(data_id, data_data_id)


def log(log_content, executor_data_id=None):
    """
    记录日志
    :param log_content:
    :param executor_data_id:
    :return:
    """
    if not executor_data_id:
        executor_data_id = global_data.executor_data_id
    logging.warning("execute_data_id: %s log_content: %s" % (executor_data_id, log_content))
    # TODO 持久化日志内容


def write_data_data_2_file(data_data, file_path):
    """
    将数据对象转json并存储到文件
    :param data_data:
    :param file_path:
    :return:
    """
    data_data_str = json.dumps(data_data, ensure_ascii=False)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data_data_str)


def execute_remote_command(host_conf, command):
    """
    执行远程shell
    :param host_conf: 远程主机信息
    :param command: shell脚本命令
    :return:
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host_conf['ip'], int(host_conf['port']), host_conf['username'], host_conf['password'])
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read().decode('utf-8')
    ssh.close()
    return result


def prepare_local_dirs(dir_list):
    """
    准备本地目录列表
    :param dir_list:
    :return:
    """
    for item in dir_list:
        if not os.path.exists(item):
            os.makedirs(item)


def declare_remote_dirs(host_conf, dir_list, permission=None):
    """
    准备远程目录列表
    :param host_conf:
    :param dir_list:
    :param permission:
    :return:
    """
    dir_list_str = " "
    for item in dir_list:
        dir_list_str += item + " "
    command_str = "mkdir -p " + dir_list_str
    if permission:
        command_str += " && chmod %s -R %s" % (permission, dir_list_str)
    return execute_remote_command(host_conf, command_str)


def get_local_files(local_dir, is_top_level=True):
    """
    获取本地目录中文件列表(不区分文件或者文件夹)
    :param local_dir:
    :param is_top_level:
    :return:
    """
    all_files = []
    if is_top_level:
        all_files.append(local_dir + "/")
    files = os.listdir(local_dir)
    for x in files:
        filename = local_dir + "/" + x
        if os.path.isdir(filename):
            all_files.append(filename + "/")
            all_files.extend(get_local_files(filename, False))
        else:
            all_files.append(filename)
    return all_files


def convert_local_files_2_remote_files(local_files, local_basic_dir, remote_basic_dir):
    """
    转换本地目录为远程目录
    :param local_files:
    :param local_basic_dir:
    :param remote_basic_dir:
    :return:
    """
    result = []
    for item in local_files:
        result.append(item.replace(local_basic_dir, remote_basic_dir))
    return result


def sync_dirs_2_remote(host_conf, local_basic_dir, remote_basic_dir, dir_name_list):
    """
    同步本地文件夹列表到远程服务器
    两种实现方式, 判断条件为文件夹中文件数量是否超过一定数量
    1、当超过时, 打包文件夹成tar包, 传输tar包到远程服务器指定的目录, 解压tar包
    2、当没超过时, 遍历文件夹进行单个传输到指定路径
    :param host_conf:
    :param local_basic_dir:
    :param remote_basic_dir:
    :param dir_name_list:
    :return:
    """
    if not isinstance(dir_name_list, list):
        raise MyServiceException("目录名称参数必须为数组")
    t = paramiko.Transport(sock=(host_conf['ip'], int(host_conf['port'])))
    t.connect(username=host_conf['username'], password=host_conf['password'])
    sftp = paramiko.SFTPClient.from_transport(t)
    for dir_name in dir_name_list:
        # 先移除, 保险起见应该是先上传到该同级_upload_temp路径, 再删除
        execute_remote_command(host_conf, "rm -rf " + remote_basic_dir + "/" + dir_name)
        local_files = get_local_files(local_basic_dir + "/" + dir_name)
        remote_files = convert_local_files_2_remote_files(local_files, local_basic_dir, remote_basic_dir)
        for index in range(len(local_files)):
            local_file = local_files[index]
            remote_file = remote_files[index]
            if local_file.endswith("/"):
                try:
                    sftp.mkdir(remote_file[:-1])
                except IOError:
                    pass
                continue
            log("sftp putting %s to %s" % (local_file, remote_file))
            sftp.put(local_file, remote_file)
            log("sftp putted %s to %s" % (local_file, remote_file))
    log("sync local:[%s] to remote:[%s] dirs:[%s] success" % (
        str(local_basic_dir), str(remote_basic_dir), str(dir_name_list)))
    # 关闭sftp
    sftp.close()
    t.close()


def sync_files_2_remote(host_conf, local_basic_dir, remote_basic_dir, file_name_list):
    """
    同步文件列表到服务器
    :param host_conf:
    :param local_basic_dir:
    :param remote_basic_dir:
    :param file_name_list:
    :return:
    """
    if not isinstance(file_name_list, list):
        raise MyServiceException("文件名称参数必须为数组")
    t = paramiko.Transport(sock=(host_conf['ip'], int(host_conf['port'])))
    t.connect(username=host_conf['username'], password=host_conf['password'])
    sftp = paramiko.SFTPClient.from_transport(t)
    for file_name in file_name_list:
        local_file = local_basic_dir + "/" + file_name
        remote_file = remote_basic_dir + "/" + file_name
        log("sftp putting %s to %s" % (local_file, remote_file))
        sftp.put(local_file, remote_file)
        log("sftp putted %s to %s" % (local_file, remote_file))
    log("sync local:[%s] to remote:[%s] dirs:[%s] success" % (
        str(local_basic_dir), str(remote_basic_dir), str(file_name_list)))
    # 关闭sftp
    sftp.close()
    t.close()
