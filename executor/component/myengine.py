import os
import threading

import config
from distribution.component import mymysql
from engine import Runtime, Data, ENGINE_LOGIC_DIR_STR, ENGINE_LOGIC_STR

START_DEPENDENCY_DEFINE_STR = "# start dependency_define"
END_DEPENDENCY_DEFINE_STR = "#  end dependency_define"


class MyEngine(threading.Thread):
    def __init__(self, data_id, data_data_id, data_event_type, logic_id, func_name):
        threading.Thread.__init__(self)
        self.data_id = data_id
        self.data_data_id = data_data_id
        self.data_event_type = data_event_type
        self.logic_id = logic_id
        self.func_name = func_name
        self.engine_logic_dir = os.path.join(config.project_root_path, ENGINE_LOGIC_DIR_STR)
        self.local_logic_file_path = os.path.join(self.engine_logic_dir,
                                                  ENGINE_LOGIC_STR + "_" + str(self.logic_id)) + ".py"

    def init_engine_logic_dir(self):
        if not os.path.exists(self.engine_logic_dir):
            os.mkdir(self.engine_logic_dir)

    def run(self):
        engine_data = {
            "data_id": self.data_id,
            "data_data_id": self.data_data_id,
            "data_event_type": self.data_event_type,
            "logic_id": self.logic_id,
            "func_name": self.func_name,
        }
        try:
            Data.status(engine_data, "START")
            self.init_engine_logic_dir()
            self.load_logic_2_local()
            Runtime.execute_logic(engine_data)
        except Exception as e:
            Data.log(engine_data, "TRACE", str(e))

    def load_logic_2_local(self):
        parameters = {
            "logic_id": self.logic_id,
        }
        sql_result = mymysql.execute("""
                                select ded.update_time, ellfv.version
                                from designer_logic_data ded
                                left join engine_local_logic_file_version ellfv on ded.id =  ellfv.logic_id
                                where ded.id = %(logic_id)s
                                ;
                            """, parameters)
        sql_result = sql_result[0]
        update_time = sql_result["update_time"]
        version = sql_result["version"]
        parameters["version"] = update_time
        if os.path.exists(self.local_logic_file_path):
            if update_time == version:
                return
        sql_result = mymysql.execute("""
                                    select file 
                                    from designer_logic_data 
                                    where id = %(logic_id)s;
                            """, parameters)
        sql_result = sql_result[0]
        logic_file = sql_result["file"]
        with open(self.local_logic_file_path, "w") as file:
            file.write(logic_file)

        if not version:
            mymysql.execute("""
                            insert into engine_local_logic_file_version(logic_id, version) 
                            values(%(logic_id)s, %(version)s);
                                """, parameters)
        else:
            mymysql.execute("""
                            update engine_local_logic_file_version 
                            set version = %(version)s 
                            where logic_id = %(logic_id)s;
                                """, parameters)
