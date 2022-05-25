import time
from flask.views import View

class TimeView(View):
    methods = ['GET',]

    def dispatch_request(self):
        return { "time": time.time() }
