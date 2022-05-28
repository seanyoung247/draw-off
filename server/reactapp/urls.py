"""
Defines the url routes managed by this app
"""

from . import views

def add_urls(bp):
    
    bp.add_url_rule(rule='/', endpoint='home', view_func=views.Index.as_view('home'))

