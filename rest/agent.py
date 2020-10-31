import json

from flask import Blueprint

from component import form
from component import mymysql

app = Blueprint('agent', __name__, url_prefix='/agent')


@app.route('/select', methods=['POST'])
def select():
    return {"": ""}
