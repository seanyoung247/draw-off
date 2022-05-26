from . import views
from flask import Blueprint

def add_urls(bp):
    bp.add_url_rule(
        rule="/time",
        endpoint='time',
        view_func=views.TimeView.as_view('time')
    )