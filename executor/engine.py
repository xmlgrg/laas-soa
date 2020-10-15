import json

from flask import Blueprint, make_response

from distribution.component import mymysql
from distribution.component import form
from distribution.exception import MyServiceException
from .component.myengine import MyEngine

app = Blueprint('engine_engine', __name__,
                url_prefix='/engine/engine')


@app.route('/trigger', methods=['POST'])
def trigger():
    try:
        request_data = form.check(['data_id', 'data_data_id', 'type', 'logic_id', 'func_name'])

        data_id = request_data["data_id"]
        data_data_id = request_data["data_data_id"]
        type = request_data["type"]
        logic_id = request_data["logic_id"]
        func_name = request_data["func_name"]

        MyEngine(data_id, data_data_id, type, logic_id, func_name).start()
        return "SUCCESS"
    except MyServiceException as e:
        print("e.msg: ", e.msg)
        custom_res = make_response(e.msg)
        custom_res.status = "500"
        return custom_res


@app.route('/select_engine_data_logic_trigger_status_details_status', methods=['POST'])
def select_engine_data_logic_trigger_status_details_status():
    request_data = form.check(['data_id', 'data_data_id'])
    return json.dumps(mymysql.execute("""
                select id,
                       data_id,
                       data_data_id,
                       data_event_type,
                       logic_id,
                       func_name,
                       DATE_FORMAT(create_time, '%%Y-%%m-%%d %%T') as create_time_str,
                       status
                from engine_data_logic_trigger_data_status
                where data_id = %(data_id)s and data_data_id = %(data_data_id)s
                order by id asc
    """, request_data))


@app.route('/select_engine_data_logic_trigger_status_details_log', methods=['POST'])
def select_engine_data_logic_trigger_status_details_log():
    request_data = form.check(['data_id', 'data_data_id', 'data_event'])
    data_event = request_data['data_event']
    sql = """
                   select log
                   from engine_data_logic_trigger_data_log
                   where 1=1
                        and data_id = %(data_id)s
                        and data_data_id = %(data_data_id)s
    """
    if 'tree' == data_event:
        pass
    elif 'data_event' == data_event:
        sql += 'and data_event_type = %(data_event_type)s'
    elif 'logic' == data_event:
        sql += """
                    and data_event_type = %(data_event_type)s
                    and logic_id = %(logic_id)s
                    and func_name = %(func_name)s
        """
    elif 'data_status' == data_event:
        sql += """
                    and data_event_type = %(data_event_type)s
                    and logic_id = %(logic_id)s
                    and func_name = %(func_name)s
                    and create_time >= str_to_date(%(create_time_str)s, '%%Y-%%m-%%d %%T')
        """
    return json.dumps(mymysql.execute(sql, request_data))
