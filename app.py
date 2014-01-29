# -*- coding: utf-8 -*-
"""
app.py
~~~~~~

:copyright: (c) 2014 by @zizzamia
"""
from flask import request, session, g, redirect, url_for, abort, render_template

# Imports modules
import config
from shared import app

# Imports routes
from routes.home import home

# Imports api
from api.timeline import timeline

LIST_MODULES = [timeline,
                home] 

@app.errorhandler(404)
def not_found(error):
    """
    Raise if a resource does not exist and never existed.

    """
    return render_template('404.html'), 404

for module in LIST_MODULES:
    app.register_blueprint(module)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT)
