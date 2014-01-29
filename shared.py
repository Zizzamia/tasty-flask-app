# -*- coding: utf-8 -*-
"""
shared.py
~~~~~~
Shared contains the variables that are shared with many modules.

:copyright: (c) 2014 by @zizzamia
"""
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')
