#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import string

template = """#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session, flash

app = Flask(__name__)
"""

secret_key = raw_input("you secret key (use random key as default):")

if secret_key == "":
    for i in range(32):
        secret_key += random.choice(string.printable[:62])

template += """
app.secret_key = '%s'
""" % secret_key

template += """
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get")
def getAction():
    param = request.args.get("param", "0")
    return param

@app.route("/post", methods=['POST'])
def postAction():
    data = request.form["data"]
    return data

"""

port = int(raw_input("web port:"))

template += """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=%d, debug=True)
""" % port

with open("app.py", "w") as f:
    f.write(template)

m = raw_input("make static and template dir? [y/n]")

if m != "y":
    exit()

os.mkdir("static")
os.mkdir(os.path.join(".", "static", "img"))
os.mkdir(os.path.join(".", "static", "css"))
os.mkdir(os.path.join(".", "static", "js"))
os.mkdir("templates")

bower = """
{
  "directory": "bower"
}
"""

with open(os.path.join(".", "static", ".bowerrc"), "w") as f:
    f.write(bower)

with open(os.path.join(".", "templates", "index.html"), "w") as f:
    pass
