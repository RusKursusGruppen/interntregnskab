# -*- coding: utf-8 -*-
from app.utils.misc import db, local
import app.utils.date as dateutils
from app.config.generated import config
from hashlib import sha224

def authenticate(username, password):
    password = sha224(password).hexdigest()
    for x in db().view("user/auth", key=[username, password]):
        return x.id

def haschangedpasswd(uid):
    return db()[uid]["has_changed_password"]

def add(username, group, password):
    password = sha224(password).hexdigest()
    db().save({
        "type": "user",
        "group": group,
        "password": password,
        "username": username,
        "date_added": dateutils.nowtuple(),
        "has_changed_password": False
    })


def changepassword(uid, password):
    password = sha224(password).hexdigest()
    user = db()[uid]
    user["has_changed_password"] = True
    user["password"] = password
    db().save(user)
    
def getname(uid):
    name = local.cache.get(("uid-name",uid))
    if name is None:
        name = db()[uid]["username"]
        local.cache[("uid-name", uid)] = name
    return name

def getgroup(uid):
    return db()[uid]["group"]

def getmembers(uid):
    group = getgroup(uid)
    q = db().view("user/group", startkey=[group], endkey=[group+u"\fff0"], include_docs=True)

    for x in q:
        doc = x.doc
        yield doc.id, doc["username"]
