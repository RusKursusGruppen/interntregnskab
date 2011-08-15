# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect
from app.utils.currency import parsenumber
import app.model.entries as entries
import app.model.user as user

def new_form():
    members = user.getmembers(local.session.get("group"))
    template_response("/page/entries/new.mako",
        members=members
    )


def new_do():
    creditor = local.request.form.get("creditor")
    amount = local.request.form.get("amount", "")
    
    if amount == "":
        amount = 0
    else:
        amount = parsenumber(amount)

    debtors = {}
    for name, weight in local.request.form.items():
        if not name.startswith("member_"):
            continue

        name = name[7:]
        weight = int(weight)
        
        if weight == 0:
            continue

        debtors[name] = weight
    
    author = local.session.get("user")
    group = local.session.get("group")
    
    entries.add(author, group, amount, creditor, debtors)

    template_response("/page/test.mako", test=(debtors, creditor, amount))
    return
    redirect("index.index")
