# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers.account
import app.controllers.usage
import app.controllers.product
import app.controllers.index
import app.controllers.misc
import app.controllers.version
import app.controllers.help

endpoints = {
    "index.index": app.controllers.index.index,
    "misc.login_form": app.controllers.misc.login_form,
    "misc.login_do": app.controllers.misc.login_do,
    "notfound": app.controllers.misc.notfound,
    "error": app.controllers.misc.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/", "index.index"),
        ("GET", "/login", "misc.login_form"),
        ("POST", "/login_do", "misc.login_do")
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)
