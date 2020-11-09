"""
执行器 执行业务

暂时为硬编码实现业务
后续改为流通数据到业务中, 执行业务
"""
import json
import threading
import time

from flask import Blueprint

from business_hardcode.build_project import build_project
from component import form

app = Blueprint('operate_executor_execute', __name__,
                url_prefix='/operate/executor/data')

business_hardcode_pool = {
    "build_project": build_project.build_project,
}


@app.route('/insert', methods=['POST'])
def insert():
    """
    执行业务, 向执行队列中添加一个执行任务
    :return:
    """
    request_data = form.check(['business_id', "data_id", "data_data_id"])  # 校验是否传入 业务id, 数据模型数据id
    data_id = request_data["data_id"]
    business_id = request_data["business_id"]
    data_data_id = request_data["data_data_id"]
    executor_data_id = time.time_ns()  # 执行器数据id, 后续包含: 执行日志、执行状态 等等
    threading.Thread(target=business_hardcode_pool[business_id],
                     args=(executor_data_id, data_id, data_data_id,)).start()
    return json.dumps({
        "executor_data_id": executor_data_id
    })
