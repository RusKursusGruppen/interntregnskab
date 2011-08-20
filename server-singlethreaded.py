#!/usr/bin/python2 -B
# -*- coding: utf-8 -*-
import sys
from os.path import dirname, join

# Prepend 3rd-party to path
sys.path[0] = join(dirname(__file__))
sys.path.insert(0, join(sys.path[0], "3rd-party"))

from app.application import Application
from wsgiref.simple_server import make_server

app = Application(debug=True)
bind_address = "127.0.0.1"
port = 5000

httpd = make_server(bind_address, port, app)

httpd.serve_forever()
