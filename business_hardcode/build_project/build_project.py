"""
构建项目

需要依赖一些数据
    构建服务器
    源码仓库信息
    项目配置信息
"""
import os
import traceback

from rest.operate.executor import context

local_executor_root_path = os.path.join(os.getcwd(), "business_hardcode/build_project")
remote_executor_root_path = "/data/tristan/1"  # 远程执行器根目录
# 准备本地目录
local_executor_data_data_path = os.path.join(local_executor_root_path, "data_data")
context.prepare_local_dirs([local_executor_data_data_path])


def build_project(executor_data_id, data_id, data_data_id):
    # 记录全局数据
    context.global_data.executor_data_id = executor_data_id
    try:
        context.log("执行器已启动: data_id: %s data_data_id: %s" % (data_id, data_data_id))
        # 得到执行器执行时的初始业务数据
        business_data = context.select_data_by_data_id__data_data_id(data_id, data_data_id)[0]
        """
        [{'id': 8, 'git_server': '1', 'project_name': '仓库系统', 'gitlab_id': '43',
            'branches': 'master', 'tags': '', 'program_language': 'java', 'docker_registry_id': '1'}]
        """
        context.log("startup_parameters: " + str(business_data))
        # 启动执行器执行业务
        # 使用构建服务器, 连接到目标服务器
        host_build = context.select_data_by_data_id__data_data_id(15, 1)[0]  # 查询服务器连接信息
        context.log('host_build: ' + str(host_build))
        # 准备远程目录
        context.log(context.declare_remote_dirs(host_build, [remote_executor_root_path]))
        # 连接到执行器
        # 获取最新版本的数据, 保存数据到本地, 同步最新版本的数据到执行器目录
        """
        data_data:
            git_server.json
            docker_registry.json
        """
        # git服务器
        data_data_git_server = context.select_data_by_data_id__data_data_id('5', business_data['git_server'])[0]
        context.write_data_data_2_file(data_data_git_server, local_executor_data_data_path + '/git_server.json')
        # docker镜像仓库
        data_data_docker_registry = \
            context.select_data_by_data_id__data_data_id('4', business_data['docker_registry_id'])[0]
        context.write_data_data_2_file(data_data_docker_registry,
                                       local_executor_data_data_path + '/docker_registry.json')
        context.sync_dirs_2_remote(host_build, local_executor_root_path, remote_executor_root_path, ["data_data"])

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

        do_build_project(executor_data_id, business_data, host_build)
    except Exception as e:
        traceback.print_exc()
        context.log(str(e))


def do_build_project(executor_data_id, business_data, host_build):
    # # 测试
    context.log(context.execute_remote_command(host_build, 'ls -alh /'))
