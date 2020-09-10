#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docs.base import Base


class Python(Base):

    _doc = {
        "virtual env": """virtualenv --no-site-packages venv
. venv/bin/activate""",
        "pip": """pip freeze > requirements.txt
pip install -r requirements.txt
pip install -U
pip install --upgrade
pip install --force-reinstall
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx
pip install -i https://mirrors.aliyun.com/pypi/simple xxxx

pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
""",
        "jupyter": """sudo jupyter notebook --ip 0.0.0.0 --allow-root""",
        "upload package": """rm -rf dist
python setup.py sdist
python -m twine upload dist/*

# for test
python -m twine upload --repository testpypi dist/*""",
        "django": """django startproject name
python manage.py startapp name"""
    }
