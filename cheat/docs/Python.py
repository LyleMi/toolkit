#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Python(Base):

    _doc = {
        "virtual env": """
virtualenv --no-site-packages venv
. venv/bin/activate
""",
        "modules": """
python -m site
python -m json.tool

# python's document
python -m pydoc -p 8000
python -m http.server --bind 127.0.0.1 8888
""",
        "pip": """
pip freeze > requirements.txt
pip install -r requirements.txt

pip install -U / pip install --upgrade
pip install --force-reinstall

# install into user env
pip install --user xxx

# set new source
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx
pip install -i https://mirrors.aliyun.com/pypi/simple xxxx
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
""",
        "jupyter": """
sudo jupyter notebook --ip 0.0.0.0 --allow-root
""",
        "debug": """
import pdb
pdb.set_trace()

# Debug the Python program given by pyfile
python -m pdb example.py

# inspect interactively after running script
python -i example.py
""",
        "upload package": """
rm -rf dist
python setup.py sdist
python -m twine upload dist/*

# for test
python -m twine upload --repository testpypi dist/*""",
        "django": """
django startproject name
python manage.py startapp name

# enable https

pip install django-secure django-sslserver

INSTALLED_APPS += ['djangosecure', 'sslserver']

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
)
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

python manage.py runsslserver
"""
    }
