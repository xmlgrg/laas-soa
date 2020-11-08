"""
构建项目

需要依赖一些数据
    构建服务器
    源码仓库信息
    项目配置信息
"""
from rest.operate.executor import context


def build_project(executor_data_id, data_id, data_data_id):
    context.log(executor_data_id,
                "executor_data_id: %s data_id: %s data_data_id: %s" % (executor_data_id, data_id, data_data_id))
    # 得到执行数据
    business_data = context.get_startup_parameters(data_id, data_data_id)
    context.log(executor_data_id, "startup_parameters: " + str(business_data))
    # 连接到目标服务器
