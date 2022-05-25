from . import views
from .blueprint import time_bp

time_bp.add_url_rule(
    rule="/time",
    endpoint='time',
    view_func=views.TimeView.as_view('time')
)