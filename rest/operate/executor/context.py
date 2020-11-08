import logging

from rest.operate.cmdb import data

"""
上下文环境
"""


def get_startup_parameters(data_id, data_data_id):
    """
    得到业务数据
    :param data_id:
    :param data_data_id:
    :return:
    """
    return data.select_by_data_id__data_data_id(data_id, data_data_id)


def log(execute_data_id, log_content):
    logging.warning("execute_data_id: %s log_content: %s" % (execute_data_id, log_content))
    # TODO 记录日志
