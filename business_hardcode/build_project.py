"""
构建项目

需要依赖一些数据
    构建服务器
    源码仓库信息
    项目配置信息
"""
import logging


def build_project(executor_data_id, data_id, data_data_id):
    logging.warning("executor_data_id: %s data_id: %s data_data_id: %s" % (executor_data_id, data_id, data_data_id))
