# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.index
import app.controllers.login
import app.controllers.misc
import app.controllers.entries

endpoints = {
    "index.index": app.controllers.index.index,
    "login.form": app.controllers.login.form,
    "login.authenticate": app.controllers.login.authenticate,
    "entries.new_form": app.controllers.entries.new_form,
    "entries.new_do": app.controllers.entries.new_do,
    "notfound": app.controllers.misc.notfound,
    "error": app.controllers.misc.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/", "index.index"),
        ("GET", "/login", "login.form"),
        ("POST", "/login_do", "login.authenticate"),
        ("GET", "/new", "entries.new_form"),
        ("POST", "/new/do", "entries.new_do")
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
