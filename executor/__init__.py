import importlib
import os

from distribution.component import mymysql

ENGINE_LOGIC_DIR_STR = "engine_logic_dir"
ENGINE_LOGIC_STR = "engine_logic"


class Runtime(object):
    @staticmethod
    def define_dependencies(dependencies):
        for item in dependencies:
            try:
                importlib.import_module(item)
            except Exception as e:
                os.system("pip install %s" % item)
                raise e

    @staticmethod
    def require(module_name):
        return importlib.import_module(module_name)

    @staticmethod
    def execute_logic(engine_data):
        try:
            Data.log(engine_data, "TRACE", "execute_logic: %s:%s for data: %s:%s:%s" % (
                engine_data["logic_id"], engine_data["func_name"], engine_data["data_id"],
                engine_data["data_data_id"], engine_data["logic_id"],))
            Data.status(engine_data, "RUNNING")
            module_name = ENGINE_LOGIC_DIR_STR + "." + ENGINE_LOGIC_STR + "_" + str(
                engine_data["logic_id"])
            module = importlib.import_module(module_name)
            target_func = getattr(module, engine_data["func_name"])
            target_func(engine_data)
            Data.status(engine_data, "FINISH")
        except Exception as e:
            Data.log(engine_data, "TRACE", str(e))
            Data.status(engine_data, "EXCEPTION")


class Data(object):
    @staticmethod
    def set(sql, parameters={}):
        print("Data: ", "sql: ", sql, "parameters: ", parameters)
        return mymysql.execute(sql, parameters)

    @staticmethod
    def get(sql, parameters={}):
        print("Data: ", "sql: ", sql, "parameters: ", parameters)
        return mymysql.execute(sql, parameters)

    @staticmethod
    def status(engine_data, cur_status):
        print("Data: ", "status: ", "engine_data: ", str(engine_data), "cur_status: ", cur_status)
        mymysql.execute("""
        insert into engine_data_logic_trigger_data_status(data_id, data_data_id, data_event_type, logic_id, func_name, status)
        values(%(data_id)s, %(data_data_id)s, %(data_event_type)s, %(logic_id)s, %(func_name)s, %(status)s)
        """, {
            "data_id": engine_data["data_id"],
            "data_data_id": engine_data["data_data_id"],
            "data_event_type": engine_data["data_event_type"],
            "logic_id": engine_data["logic_id"],
            "func_name": engine_data["func_name"],
            "status": cur_status,
        })

    @staticmethod
    def log(engine_data, log_level="TRACE", log_content=""):
        print("log: ", "engine_data: ", str(engine_data), "log_level: ", log_level, "log_content: ", log_content)
        mymysql.execute("""
        insert into engine_data_logic_trigger_data_log(data_id, data_data_id, data_event_type, logic_id, func_name, log_level, log)
        values(%(data_id)s, %(data_data_id)s, %(data_event_type)s, %(logic_id)s, %(func_name)s, %(log_level)s, %(log)s)
        """, {
            "data_id": engine_data["data_id"],
            "data_data_id": engine_data["data_data_id"],
            "data_event_type": engine_data["data_event_type"],
            "logic_id": engine_data["logic_id"],
            "func_name": engine_data["func_name"],
            "log_level": log_level,
            "log": log_content,
        })

# TODO refactor the code to increase the engine project, now is too weak

