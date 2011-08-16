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

for rustur, vejledere in (
    ("lerustour", (
        "alexandra",
        "bjorn",
        "efs",
        "hk",
        "jenny",
        "lund",
        "mark",
        "sdahlgaard"
    )),
    ("diwinger", (
        "ahmed",
        "davy",
        "henrik",
        "kirstejn",
        "jens",
        "caro",
        "martin",
        "soren",
        "steph"
    )),
    ("prinsesseturen", (
        "christina",
        "daniel",
        "ejnar",
        "kristoffer",
        "lasse",
        "peter",
        "martin",
        "markus",
    )),
):
    for vejleder in vejledere:
        password = generate_password()
        user.add(vejleder, rustur, password)
        print "Brugernavn: %s" % (vejleder,)
        print "Password: %s" % (password,)
        print "-"*40
