def init(app):
    from rest import ping
    from rest.operate.business import data as operate_business_data
    from rest.operate.business import directory as operate_business_directory
    from rest.operate.cmdb import data as operate_cmdb_data
    from rest.operate.cmdb import directory as operate_cmdb_directory
    from rest.operate.cmdb import struct as operate_cmdb_struct
    from rest.operate.executor import data as operate_executor_data
    from rest import agent

    # ################### 注册路由
    app.register_blueprint(ping.app)
    # 数据模型
    app.register_blueprint(operate_cmdb_data.app)
    app.register_blueprint(operate_cmdb_directory.app)
    app.register_blueprint(operate_cmdb_struct.app)
    # 业务脚本
    app.register_blueprint(operate_business_data.app)
    app.register_blueprint(operate_business_directory.app)
    # 执行器
    app.register_blueprint(operate_executor_data.app)
    # agent
    app.register_blueprint(agent.app)
