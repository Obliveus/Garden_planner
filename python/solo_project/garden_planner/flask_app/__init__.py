from flask import Flask, session
from env import KEY
app = Flask(__name__)
app.secret_key = KEY

UPLOAD_FOLDER = '/static/img/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024