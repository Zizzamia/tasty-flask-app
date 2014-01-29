# -*- coding: utf-8 -*-
"""
timeline.py
~~~~~~

:copyright: (c) 2014 by @zizzamia
"""
from flask import Blueprint, request, jsonify

timeline = Blueprint('timeline', __name__)

timeline_list = [
    {"username": "zizzamia", 
     "text": "I just set my personal app"},
    {"username": "zizzamia", 
     "text": "I love Nutella"}
]

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

def get_timeline():
    """ """
    data = {
        "success": True,
        "list_tweet": timeline_list
    }
    return data

def post_timeline():
    """ """
    username = request.json.get("username", None)
    text = request.json.get("text", None)
    if username and text:
        tweet = {
            "username": username,
            "text": text
        }
        timeline_list.append(tweet)
        data = {
            "success": True,
            "list_tweet": timeline_list
        }
    else:
        data = {
            "success": False,
            "list_tweet": timeline_list
        }
    return data

def delete_timeline(index):
    """ """
    if index >= 0 and index < len(timeline_list):
        timeline_list.pop(index)
        data = {
            "success": True,
            "list_tweet": timeline_list
        }
    else:
        data = {
            "success": False,
            "message": "Wrong"
        }
    return data