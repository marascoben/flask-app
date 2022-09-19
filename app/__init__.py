import flask
import os
from settings import DEBUG

web = flask.Flask(__name__, static_url_path='/static')

if DEBUG:
    web.secret_key = b'secret_key#'
else:
    web.secret_key = os.urandom(24)

@web.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')

