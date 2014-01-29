# -*- coding: utf-8 -*-
"""
timeline.py
~~~~~~

:copyright: (c) 2014 by @zizzamia
"""
import time
from flask import Blueprint, request, jsonify
from model.timeline import TimelineStorage

timeline_storage = TimelineStorage()

timeline = Blueprint('timeline', __name__)

@timeline.route('/api/timeline', methods=['GET', 'POST', 'DELETE'])
@timeline.route('/api/timeline/<int:index>/', methods=['GET', 'POST', 'DELETE'])
def api(index=None):
    """ """
    if request.method == "GET":
        data = get_timeline()
    elif request.method == "POST":
        data = post_timeline()
    elif request.method == "DELETE":
        data = delete_timeline(index)
    return jsonify(data)

@timeline.route('/api/timeline/restart/', methods=['GET'])
def restart():
    """ """
    timeline_storage.restart()
    data = {
        "success": True,
        "list_tweet": timeline_storage.get(),
        "seconds_to_restart": 30
    }
    return jsonify(data)

def get_timeline():
    """ """
    time_now = int(time.time()) - timeline_storage.last_restart
    seconds_to_restart = int(30 - time_now)
    seconds_to_restart = seconds_to_restart if seconds_to_restart > 0 else 0
    data = {
        "success": True,
        "seconds_to_restart": seconds_to_restart,
        "list_tweet": timeline_storage.get()
    }
    return data

def post_timeline():
    """ """
    username = request.json.get("username", None)
    text = request.json.get("text", None)
    if username and text:
        timeline_storage.add(username=username, text=text)
        data = {
            "success": True,
            "list_tweet": timeline_storage.get()
        }
    else:
        data = {
            "success": False,
            "list_tweet": timeline_storage.get()
        }
    return data

def delete_timeline(index):
    """ """
    if index >= 0 and index < len(timeline_storage.get()):
        timeline_storage.delete(index=index)
        data = {
            "success": True,
            "list_tweet": timeline_storage.get()
        }
    else:
        data = {
            "success": False,
            "message": "Wrong"
        }
    return data
