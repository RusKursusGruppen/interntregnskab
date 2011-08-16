#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
import os
sys.path[0] = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(sys.path[0], "3rd-party"))
os.chdir(sys.path[1])

import app.model.user as user

from app.config.generated import config
from random import choice

def generate_password(chars="ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789", length=10):
    return "".join(choice(chars) for x in range(length))
        
while True:
    username = raw_input("Indtast brugernavn: ")
    username = username.strip()
    if len(username) != 0: break

while True:
    group = raw_input("Indtast gruppe: ")
    group = group.strip()
    
    if len(group) != 0: break


password = generate_password()
print
print
print

print "Brugernavn: %s" % (repr(username),)
print "Gruppe: %s" % (repr(group),)
print "Midlertidig adgangskode: %s" % (repr(password),)

user.add(username, group, password)
