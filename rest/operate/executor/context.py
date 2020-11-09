import json
import logging

from rest.operate.cmdb import data

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


def log(execute_data_id, log_content):
    """
    记录日志
    :param execute_data_id:
    :param log_content:
    :return:
    """
    logging.warning("execute_data_id: %s log_content: %s" % (execute_data_id, log_content))
    # TODO 记录日志


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
