# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect, db
import app.model.user as user

def form():
    error_length = local.request.args.get("length") != None
    error_invalid = local.request.args.get("invalid") != None
    
    template_response("/page/login.mako",
        error_length = error_length,
        error_invalid = error_invalid
    )


def authenticate():
    error = {}

    username = local.request.form.get("username", u"")
    password = local.request.form.get("password", u"")
    
    if len(username) == 0 or len(password) == 0:
        error["length"] = "yes"
    
    if len(error) == 0:
        uid = user.authenticate(username, password)
        if uid is None:
            error["invalid"] = "yes"
    
    if len(error) == 0:
        local.session["uid"] = uid
        
        if not user.haschangedpasswd(uid):
            redirect("login.chpasswd_form")
            return

        redirect("index.index")
        return

    redirect(
        "login.form",
        **error
    )


def chpasswd_form():
    error_match = local.request.args.get("match") != None
    error_length = local.request.args.get("length") != None
    
    first_time = not user.haschangedpasswd(local.session.get("uid"))

    template_response("/page/change_passwd.mako",
        error_match=error_match,
        error_length=error_length,
        first_time=first_time
    )


def chpasswd_confirm():
    template_response("/page/change_passwd_confirm.mako")


def chpasswd_do():
    password0 = local.request.form.get("password0", u"")
    password1 = local.request.form.get("password1", u"")
    
    error = {}

    if len(password0) == 0 or len(password1) == 0:
        error["length"] = "yes"
    
    if len(error) == 0 and password0 != password1:
        error["match"] = "yes"
    
    if len(error) == 0:
        user.changepassword(local.session.get("uid"), password0)
        redirect("login.chpasswd_confirm")
        return
    
    redirect(
        "login.chpasswd_form",
        **error
    )


def logout():
    local.session["uid"] = None
    redirect("login.chpasswd_form")
