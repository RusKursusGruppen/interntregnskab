#!/usr/bin/python2
# -*- coding: utf-8 -*-
import env

from werkzeug import run_simple
from app.application import Application

app = Application(debug=False)
bind_address = "0.0.0.0"
port = 5000

run_simple(
    bind_address, port, app, use_debugger=False, use_reloader=False
)

