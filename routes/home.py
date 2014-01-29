# -*- coding: utf-8 -*-
"""
home.py
~~~~~~

:copyright: (c) 2014 by @zizzamia
"""
from flask import Blueprint, request, g, render_template

home = Blueprint('home', __name__)

@home.route('/')
def index():
    """ """
    title = "My custom Timeline"
    return render_template('index.html', title=title)
