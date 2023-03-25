import base64
import os

from flask import Flask
from flask import render_template, request
from PIL import Image
import cv2
import numpy as np
import io
from flask import current_app as session
import os
from flask_cors import CORS, cross_origin
import json
import requests as rq
from lxml import etree
import random
import time
import shutil
from utils.database import isNeedRegister, registerAccount
from utils.database import data_root as database_root

app = Flask(__name__, static_folder='static')
app.debug = True
app.secret_key = os.urandom(24)
CORS(app, resources='/*', origins='*', methods=['GET', 'POST'])

os.makedirs(database_root, exist_ok=True)

import flask

print(flask.__version__)



@cross_origin
@app.route("/register",methods=["POST"])
def register():
    user_name = request.args.get('nick_name')
    needRegister = isNeedRegister(user_name)
    if needRegister:
        registerAccount(user_name)
    return "0"



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=50001)
