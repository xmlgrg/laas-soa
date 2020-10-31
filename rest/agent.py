import json

from flask import Blueprint

from component import form
from component import mymysql

app = Blueprint('agent', __name__, url_prefix='/agent')


@app.route('/consume_thing', methods=['POST'])
def consume_thing():
    return json.dumps({"test": "test"})
