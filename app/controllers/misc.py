# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect
from app.model.user import authenticate

def error():
    template_response("/error/error.mako")


def notfound():
    local.response.status_code = 404
    template_response("/error/notfound.mako")


def login_form():
    error_length = local.request.args.get("length") != None
    error_invalid = local.request.args.get("invalid") != None
    

    user = local.session.get("user")

    if user != None:
        return

    template_response("/page/login.mako",
        error_length = error_length,
        error_invalid = error_invalid
    )


def login_do():
    error= {}

    username = local.request.form.get("username", u"")
    password = local.request.form.get("password", u"")
    
    if len(username) == 0 or len(password) == 0:
        error["length"] = "yes"
    
    if len(error) == 0 and not authenticate(username, password):
        error["invalid"] = "yes"
    
    if len(error) == 0:
        local.session["user"] = username
        return

    redirect(
        "misc.login_form",
        **error
    )
    
