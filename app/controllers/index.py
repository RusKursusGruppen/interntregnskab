# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

def index():
    template_response("/page/index.mako")
