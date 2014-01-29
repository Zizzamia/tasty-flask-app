# -*- coding: utf-8 -*-
"""
timeline.py
~~~~~~

:copyright: (c) 2014 by @zizzamia
"""
import time

class TimelineStorage(object):
    """ This class allows to :
    - get
    - restart
    """

    def __init__(self):
        """ """
        self.timeline_list = [
            {"username": "zizzamia", 
             "text": "I just set my personal app"},
            {"username": "zizzamia", 
             "text": "I love Nutella"}
        ]
        self.last_restart = int(time.time())

    def get(self):
        """ """
        return self.timeline_list

    def add(self, username="test", text="test text"):
        """ """
        self.timeline_list.append({
            "username": username,
            "text": text
        })

    def delete(self, index=0):
        """ """
        self.timeline_list.pop(index)

    def restart(self):
        """ """
        self.last_restart = int(time.time())
        self.timeline_list = [
            {"username": "zizzamia", 
             "text": "I just set my personal app"},
            {"username": "zizzamia", 
             "text": "I love Nutella"}
        ]
