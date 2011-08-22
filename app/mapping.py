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
    "login.logout": app.controllers.login.logout,
    "login.chpasswd_form": app.controllers.login.chpasswd_form,
    "login.chpasswd_do": app.controllers.login.chpasswd_do,
    "login.chpasswd_confirm": app.controllers.login.chpasswd_confirm,
    "entries.new_form": app.controllers.entries.new_form,
    "entries.new_do": app.controllers.entries.new_do,
    "entries.delete": app.controllers.entries.delete,
    "notfound": app.controllers.misc.notfound,
    "error": app.controllers.misc.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET" , "/", "index.index"),
        ("GET" , "/login", "login.form"),
        ("POST", "/login_do", "login.authenticate"),
        ("GET" , "/logout", "login.logout"),
        ("GET" , "/new", "entries.new_form"),
        ("POST", "/new/do", "entries.new_do"),
        ("GET" , "/delete/<string:id>", "entries.delete"),
        ("GET" , "/chpasswd", "login.chpasswd_form"),
        ("GET" , "/chpasswd/confirm", "login.chpasswd_confirm"),
        ("POST", "/chpasswd/do", "login.chpasswd_do")
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
