"""
构建项目

需要依赖一些数据
    构建服务器
    源码仓库信息
    项目配置信息
"""
import os
import traceback

import paramiko

from rest.operate.executor import context


def prepare_dir_list(dir_list):
    for item in dir_list:
        if not os.path.exists(item):
            os.makedirs(item)


local_path = os.path.join(os.getcwd(), "business_hardcode/build_project")
local_data_data_path = os.path.join(local_path, "data_data")
prepare_dir_list([local_data_data_path])


def build_project(executor_data_id, data_id, data_data_id):
    context.log(executor_data_id,
                "执行器已启动: executor_data_id: %s data_id: %s data_data_id: %s" % (executor_data_id, data_id, data_data_id))
    # 得到执行器执行时的初始业务数据
    business_data = context.select_data_by_data_id__data_data_id(data_id, data_data_id)[0]
    # [{'id': 8, 'git_server': '1', 'project_name': '仓库系统', 'gitlab_id': '43', 'branches': 'master', 'tags': '', 'program_language': 'java', 'docker_registry_id': '1'}]
    context.log(executor_data_id, "startup_parameters: " + str(business_data))
    # 启动执行器执行业务
    # 使用构建服务器, 连接到目标服务器
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        host_build = context.select_data_by_data_id__data_data_id(15, 1)[0]  # 查询服务器连接信息
        # 连接到执行器
        ssh.connect(host_build['ip'], int(host_build['port']), host_build['username'], host_build['password'])
        # 获取最新版本的数据, 保存数据到本地, 同步最新版本的数据到执行器目录
        """
        data_data:
            git_server.json
            docker_registry.json
        """
        # git服务器
        data_data_git_server = context.select_data_by_data_id__data_data_id('5', business_data['git_server'])[0]
        context.write_data_data_2_file(data_data_git_server,
                                       os.path.join(local_data_data_path, 'git_server.json'))
        # docker镜像仓库
        data_data_docker_registry = \
            context.select_data_by_data_id__data_data_id('4', business_data['docker_registry_id'])[0]
        context.write_data_data_2_file(data_data_docker_registry,
                                       os.path.join(local_data_data_path, 'docker_registry.json'))
        # 获取最新版本的业务, 保存业务到本地, 同步最新版本的业务到执行器
        """
        business_hyper_fusion:
            java:
                do_build_project.sh
                build_project.sh
                clean_build_project.sh
                startup.sh
                Dockerfile
                do_build_docker.sh
                clean_build_docker.sh
        """

        do_build_project(executor_data_id, business_data, ssh)
    except Exception as e:
        traceback.print_exc()
        context.log(executor_data_id, str(e))
    finally:
        ssh.close()


executor_root_path = "/data/tristan"


def do_build_project(executor_data_id, business_data, ssh):
    # # 测试
    stdin, stdout, stderr = ssh.exec_command('ls -alh /')
    context.log(executor_data_id, stdout.read().decode('utf-8'))
