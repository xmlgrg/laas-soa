#!/usr/local/bin/python
# coding: utf-8
import argparse
import json
import os

parser = argparse.ArgumentParser(description='executor start up command args')
parser.add_argument('-ei', '--executor_id', nargs=1, type=int, help='executor id')
args = parser.parse_args()

executor_id = args.executor_id[0]  # 当前执行器id
root_path = os.getcwd()
cur_executor_path = os.path.join(root_path, executor_id)
# 加载数据
# 加载业务脚本, 将部分数据替换到业务脚本中, 执行业务脚本
startup_data = None


def load_startup_data():
    """
    加载启动数据
    :return:
    """
    with open(os.path.join(cur_executor_path, "data_data.json")) as f:
        global startup_data
        startup_data = json.loads(str(f.readlines()))

def load_project_source_code():

    pass

def load_business():
    pass


def business_load_data():
    pass


def execute_business():
    # do_build_project
    # build_project
    # clean_build_project
    # startup
    # Dockerfile
    # do_build_docker
    # build_docker
    # clean_build_docker
    pass


if __name__ == '__main__':
    load_startup_data()
