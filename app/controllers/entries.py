# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect

def new_form():
    template_response("/page/entries/new.mako")
    pass


def new_do():
    members = [x[7:] for x in local.request.form if x.startswith("member_")]
    creditor = local.request.form.get("creditor")
    amount = local.request.form.get("amount")

    template_response("/page/test.mako", test=(members, creditor, amount)
    return
    redirect("index.index")
