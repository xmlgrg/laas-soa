import json
import time
from threading import Lock

from flask import Blueprint

from component import form

app = Blueprint('agent', __name__, url_prefix='/agent')

business_pool = {}  # 业务池
business_status_pool = {}  # 业务状态池
business_data_pool = {}  # 业务数据池
business_execute_status_pool = {}  # 业务执行状态池
business_execute_log_pool = {}  # 业务执行状态池

consume_business_lock = Lock()


# 查询业务
@app.route('/select_business', methods=['POST'])
def select_business():
    return json.dumps({
        "business_pool": business_pool,
        "business_status_pool": business_status_pool,
        "business_data_pool": business_data_pool,
        "business_execute_status_pool": business_execute_status_pool,
        "business_execute_log_pool": business_execute_log_pool,
    })


# 新增业务
@app.route('/insert_business', methods=['POST'])
def insert_business():
    request_data = form.check(["business_type", "business_data"])
    business_type = request_data["business_type"]
    business_data = request_data["business_data"]

    business_id = int(time.time_ns())

    # 将业务插入业务池中
    if business_type not in business_pool:
        business_pool[business_type] = []
    business_pool[business_type].append(business_id)
    # 将业务数据插入业务数据池中
    if business_type not in business_data_pool:
        business_data_pool[business_type] = {}
    business_data_pool[business_type][business_id] = business_data

    return "SUCCESS"


# 消费业务
@app.route('/consume_business', methods=['POST'])
def consume_business():
    result = []
    request_data = form.check(["business_type_list"])
    business_type_list = request_data["business_type_list"]
    consume_business_lock.acquire()

    def check(business_type):
        if business_type not in business_pool:
            return False
        if len(business_pool[business_type]) < 1:
            return False
        return True

    for business_type in business_type_list:
        if not check(business_type):
            consume_business_lock.release()
            continue

        # 删除业务记录
        business_id = business_pool[business_type].pop()
        # 取出业务数据
        business_data = business_data_pool[business_type].pop(business_id)

        # 修改业务执行状态为已消费
        if business_type not in business_execute_status_pool:
            business_execute_status_pool[business_type] = {}
        business_execute_status_pool[business_type][business_id] = "CONSUMED"
        consume_business_lock.release()
        result.append({
            "business_type": business_type,
            "business_data": business_data
        })

    return json.dumps(result)
