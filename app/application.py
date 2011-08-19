# -*- coding: utf-8 -*-
from werkzeug import SharedDataMiddleware
from app.utils.misc import path
from app.utils.misc import local
from werkzeug import Request, Response
from app.mapping import url_map, endpoints
from app.utils.session import Session
from werkzeug.exceptions import NotFound
from app.utils.misc import local


class Application(object):
    def __init__(self, debug):
        self.debug = debug
        self.dispatch = SharedDataMiddleware(self.dispatch, {"/static": path["static"]})

    def dispatch(self, environ, start_response):
        try:

            local.request = Request(environ)
            local.response = Response()
            local.session = Session(local.request.cookies.get("session"), 600)
            local.cache = {}
            try:
                local.url_adapter = url_adapter = url_map.bind_to_environ(environ)
                try:
                    endpoint, params = url_adapter.match()
                except NotFound:
                    endpoint = "notfound"
                    params = {}

                if not endpoint in ("notfound", "login.authenticate") and local.session.get("uid") is None:
                    endpoint = "login.form"

                local.endpoint = endpoint

                endpoints[endpoint](**params)
            except:
                if self.debug:
                    raise
                endpoints["error"]()
            response = local.response
            local.session.save()
            local.session.set_cookie(local.response)
        except:
            if self.debug:
                raise
            response = Response("Fejlsidens fejlside.")

        return response(environ, start_response)

    def __call__(self, environ, start_response):
        local.application = self
        return self.dispatch(environ, start_response)
