"""
Defines this apps view routes
"""

from flask import send_from_directory
from flask.views import View


class Index(View):
    methods = ['GET',]
    
    def dispatch_request(self, path='index.html'):
        return send_from_directory('react', path)
