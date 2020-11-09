import json
import logging
import os
import threading

import paramiko

from rest.operate.cmdb import data

global_data = threading.local()
print(global_data)
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


def log(log_content):
    """
    记录日志
    :param execute_data_id:
    :param log_content:
    :return:
    """
    logging.warning("execute_data_id: %s log_content: %s" % (global_data.executor_data_id, log_content))
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


def prepare_remote_dirs(host_conf, dir_list, permission=None):
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


def sync_local_files_2_remote_server(host_conf, local_file_2_remote_host_list):
    """
    同步本地文件到远程服务器
    :param host_conf:
    :param local_file_2_remote_host_list:
    :return:
    """
    t = paramiko.Transport((host_conf['ip'], host_conf['port']))
    t.connect(username=host_conf['username'], password=host_conf['password'])
    sftp = paramiko.SFTPClient.from_transport(t)
    for item in local_file_2_remote_host_list:
        sftp.put(item["local"], item["remote"])
    t.close()


def get_files_in_local_dir(local_dir):
    """
    获取本地目录中文件列表
    :param local_dir:
    :return:
    """
    all_files = list()
    files = os.listdir(local_dir)
    for x in files:
        filename = os.path.join(local_dir, x)
        if os.path.isdir(x):
            all_files.extend(get_files_in_local_dir(filename))
        else:
            all_files.append(filename)
    return all_files


def sync_2_remote_dir(host_conf, local_dir, remote_dir):
    """
    同步到远程目录
    两种实现方式, 判断条件为文件夹中文件数量是否超过一定数量
        1、当超过时, 打包文件夹成tar包, 传输tar包到远程服务器指定的目录, 解压tar包
        2、当没超过时, 遍历文件夹进行单个传输到指定路径
    :return:
    """
    t = paramiko.Transport(sock=(host_conf['ip'], host_conf['port']))
    t.connect(username=host_conf['username'], password=host_conf['password'])
    sftp = paramiko.SFTPClient.from_transport(t)
    if remote_dir[-1] == '/':
        remote_dir = remote_dir[0:-1]
    files = get_files_in_local_dir(local_dir)
    for x in files:
        filename = os.path.split(x)[-1]
        remote_filename = remote_dir + '/' + filename
        sftp.put(x, remote_filename)
