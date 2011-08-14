# -*- coding: utf-8 -*-
import app.utils.pam as pam
import grp

def authenticate(username, password):
    try:
        if not username in grp.getgrnam("rkg").gr_mem:
            return False
    except KeyError:
        return False
    return pam.authenticate(username, password)


