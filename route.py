def init(app):
    from rest import ping
    # 运维
    from rest import agent
    from rest.operate.business import data as operate_business_data
    from rest.operate.business import directory as operate_business_directory
    from rest.operate.cmdb import data as operate_cmdb_data
    from rest.operate.cmdb import directory as operate_cmdb_directory
    from rest.operate.cmdb import struct as operate_cmdb_struct
    # 变更

    # 注册路由
    app.register_blueprint(ping.app)
    app.register_blueprint(agent.app)
    app.register_blueprint(operate_business_data.app)
    app.register_blueprint(operate_business_directory.app)
    app.register_blueprint(operate_cmdb_data.app)
    app.register_blueprint(operate_cmdb_directory.app)
    app.register_blueprint(operate_cmdb_struct.app)
