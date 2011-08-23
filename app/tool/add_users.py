# -*- coding: utf-8 -*-
_toolname = "add_users"
_tooldesc = "Adds a hard-coded list of users defined in app/tool/add_users.py"

import app.model.user as user

from app.config.generated import config
from random import choice

def generate_password(chars="ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789", length=10):
    return "".join(choice(chars) for x in range(length))

def main():
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
