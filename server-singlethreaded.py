#!/usr/bin/python2 -B
# -*- coding: utf-8 -*-
import env

from app.application import Application
from wsgiref.simple_server import make_server

app = Application(debug=True)
bind_address = "127.0.0.1"
port = 5000

httpd = make_server(bind_address, port, app)

httpd.serve_forever()
