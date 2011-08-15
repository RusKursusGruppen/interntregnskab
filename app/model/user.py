# -*- coding: utf-8 -*-
import app.utils.pam as pam
import grp
from app.config.generated import config

def authenticate(username, password):
    if getgroup(username) == None:
        return False
    
    if not pam.authenticate(username, password):
        return False

    return True

def getgroup(username):
    for group in config["groups"]:
        if username in getmembers(group):
            return group

def getmembers(group):
    try:
        return grp.getgrnam(group).gr_mem
    except KeyError:
        raise Exception("Group %s not found on system" % (repr(group),))
