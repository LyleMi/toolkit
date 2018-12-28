#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseDoc


class pythonDoc(BaseDoc):

    _doc = {
        "virtual env": """virtualenv venv
    . venv/bin/activate""",
        "pip": """pip freeze > requirements.txt
    pip install -r requirements.txt
    pip install -U
    pip install --upgrade
    pip install --force-reinstall
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxxx
    pip install -i https://mirrors.aliyun.com/pypi/simple xxxx
    """,
        "jupyter": """sudo jupyter notebook --ip 0.0.0.0 --allow-root
    """
    }
