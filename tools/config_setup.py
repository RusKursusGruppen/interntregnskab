#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os.path
import sys
import grp

sys.path[0] = os.path.join(os.path.dirname(__file__), "..")

def user_query(itemname, converter, defaultrep, default=None):
    while True:
        if default == None:
            answer = raw_input("Indtast %s: " % (itemname,))
        else:
            answer = raw_input("Indtast %s [%s]: " % (itemname, defaultrep(default)))
            if answer == "":
                return default
        try:
            answer = converter(answer)
        except:
            print "Kunne ikke forstå værdien, prøv igen."
            continue
        return answer

def prompt_update_config():
    try:
        from app.config.generated import config
    except ImportError:
        from app.config.default import config
        config = config()

    for name, key, converter, repr_ in [
        ("CouchDB Server URL", "couchdb_server_url", str, str),
        ("CouchDB db", "couchdb_db", str, str),
    ]:
        config[key] = user_query(name, converter, repr_, config[key])
    return config

def write_config(config):
    filename = os.path.join(os.path.dirname(__file__), "..", "app", "config", "generated.py")
    fhandle = open(filename, "w")
    fhandle.write(
        "# -*- coding: utf-8 -*-\n"
      + "from app.config.default import config\n"
      + "config = config()\n"
      + "config.update(" + repr(config) + ")"
    )

if __name__ == "__main__":
    config = prompt_update_config()
    write_config(config)
