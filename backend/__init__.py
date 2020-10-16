import os

import urllib3
from flask_cors import CORS

urllib3.disable_warnings()
# init the web framework
from flask import Flask, make_response
import logging
from logging.handlers import TimedRotatingFileHandler
from backend.exception import MyServiceException
from backend import config
from backend.component import mymysql

app = Flask(__name__, static_folder='../user/dist')

app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app, supports_credentials=True)


@app.route('/<path:path>')
def static_path(path):
    return app.send_static_file(path)


@app.route('/')
def index():
    return app.send_static_file("index.html")


@app.errorhandler(500)
def error(e):
    e = e.original_exception
    if isinstance(e, MyServiceException):
        print("e.msg: ", e.msg)
        custom_res = make_response(e.msg)
        custom_res.status = "500"
        return custom_res
    return e


from backend.service.data import directory as distribution_data_directory
from backend.service.data import struct as distribution_data_struct
from backend.service.data import data as distribution_data_data
from backend.service.logic import directory as distribution_logic_directory
from backend.service.logic import data as distribution_logic_data
from backend.service.data_logic import io as distribution_data_logic_io
from backend.service.data_logic import trigger as distribution_data_logic_trigger

# from engine import engine

app.register_blueprint(distribution_data_directory.app)
app.register_blueprint(distribution_data_struct.app)
app.register_blueprint(distribution_data_data.app)
app.register_blueprint(distribution_logic_directory.app)
app.register_blueprint(distribution_logic_data.app)
app.register_blueprint(distribution_data_logic_io.app)
app.register_blueprint(distribution_data_logic_trigger.app)
# app.register_blueprint(engine.app)

# init the log
if not os.path.exists("logs"):
    os.mkdir("logs")
formatter = logging.Formatter(
    "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
handler = TimedRotatingFileHandler(
    "logs/flask.log", when="D", interval=1, backupCount=15,
    encoding="UTF-8", delay=False, utc=True)
app.logger.addHandler(handler)
handler.setFormatter(formatter)

mymysql.init(config.app_conf["mysql"])
