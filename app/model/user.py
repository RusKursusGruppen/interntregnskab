# -*- coding: utf-8 -*-
from app.utils.misc import db
import app.utils.date as dateutils
from app.config.generated import config
from hashlib import sha224


def authenticate(username, password):
    password = sha224(password).hexdigest()
    for x in db().view("user/auth", key=[username, password]):
        return x.id

def add(username, group, password):
    password = sha224(password).hexdigest()
    db().save({
        "type": "user",
        "group": group,
        "password": password,
        "username": username,
        "date_added": dateutils.nowtuple()
    })

def getname(uid):
   return db()[uid]["username"]

def getgroup(uid):
    return db()[uid]["group"]

def getmembers(uid):
    group = getgroup(uid)
    q = db().view("user/group", startkey=[group], endkey=[group+u"\fff0"], include_docs=True)

    for x in q:
        doc = x.doc
        yield doc.id, doc["username"]
