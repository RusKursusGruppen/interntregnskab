# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect
import app.model.user as user

def form():
    error_length = local.request.args.get("length") != None
    error_invalid = local.request.args.get("invalid") != None
    

    user = local.session.get("user")

    if user != None:
        return

    template_response("/page/login.mako",
        error_length = error_length,
        error_invalid = error_invalid
    )


def authenticate():
    error= {}

    username = local.request.form.get("username", u"")
    password = local.request.form.get("password", u"")
    
    if len(username) == 0 or len(password) == 0:
        error["length"] = "yes"
    
    if len(error) == 0 and not user.authenticate(username, password):
        error["invalid"] = "yes"
    
    if len(error) == 0:
        local.session["user"] = username
        redirect("index.index")
        return

    redirect(
        "login.form",
        **error
    )
    
