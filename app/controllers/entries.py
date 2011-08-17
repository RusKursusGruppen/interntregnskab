# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect
from app.utils.currency import parsenumber
import app.model.entries as entries
import app.model.user as user

def new_form():
    members = list(user.getmembers(local.session.get("uid")))
    template_response("/page/entries/new.mako",
        members=members
    )


def new_do():
    description = local.request.form.get("description", u"")
    creditor = local.request.form.get("creditor", u"")
    amount = local.request.form.get("amount", u"")
    amount = parsenumber(amount)
    
    if amount == None:
        amount = 0

    debtors = []
    for name, weight in local.request.form.items():
        if not name.startswith("member_"):
            continue

        name = name[7:]
        weight = int(weight)
        
        if weight == 0:
            continue

        debtors.append([name, weight])
    
    username = local.session.get("uid")
    group = user.getgroup(local.session.get("uid"))
    entries.add(username, group, description, amount, creditor, debtors)

    redirect("index.index")


def delete(id):
    entries.delete(local.session.get("uid"), id)
    redirect("index.index")
