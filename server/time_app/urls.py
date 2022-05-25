from . import views
import flask

bp = flask.Blueprint(
    name="time_app",
    import_name="time_app",
)

bp.add_url_rule(
    rule="/time",
    endpoint='time',
    view_func=views.TimeView.as_view('time')
)