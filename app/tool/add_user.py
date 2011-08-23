# -*- coding: utf-8 -*-
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
