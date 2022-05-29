"""
Defines this apps view routes
"""

from flask import send_from_directory
from flask.views import View


class Index(View):
    methods = ['GET',]
    
    def dispatch_request(self, path='index.html'):
        """ Redirects calls to website root to the react package """
        return send_from_directory('build', path)
