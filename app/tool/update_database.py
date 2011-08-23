# -*- coding: utf-8 -*-
_toolname = "push_views"
_tooldesc = "Pushes whatever CouchDB javascript views it can find in ./views"

import couchdb
from itertools import groupby

from app.config.generated import config
from app.utils.folder import get_files

import os
import os.path as path

def main():
    try:
        server = couchdb.Server(config["couchdb_server_url"])
        db = server[config["couchdb_db"]]
    except couchdb.ResourceNotFound:
        db = server.create(config["couchdb_db"])
    except:
        print "Couldn't connect to couchdb."
        raise SystemExit

    views = []
    for file in get_files(directory="views"):
        content = open(file).read()
        designdoc = os.path.split(os.path.split(os.path.split(file)[0])[0])[1]
        viewname = os.path.split(os.path.split(file)[0])[1]
        type = os.path.split(file)[1][:-3]
        views += [(designdoc, type, viewname, content)]
    views.sort()

    docs = []
    for designdoc, views in groupby(views, lambda val: val[0]):
        try:
            doc = db["_design/" + designdoc]
        except couchdb.ResourceNotFound:
            doc = {}
            exists = False
        else:
            exists = True
        doc["_id"] = "_design/" + designdoc
        doc["language"] = "javascript"
        doc["views"] = {}
        for designdoc, type, viewname, content in views:
            if not viewname in doc["views"]:
                doc["views"][viewname] = {}
            doc["views"][viewname].update({type: content})
        
        if not exists or db[doc["_id"]] != doc:
            print "Updating", designdoc + ",", viewname + ",", type
            db[doc["_id"]] = doc
