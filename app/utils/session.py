# -*- coding: utf-8 -*-
from app.utils.misc import db
import app.utils.date as dateutils


class InvalidCookieException(Exception):
    pass

class Session(object):
    def __init__(self, id):
        self.id = id
        self.is_init = False
        self.changed = False
    
    def init(self):
        if self.is_init:
            return
        self.is_init = True

        self.date = dateutils.now()
        if self.id != None:
            try:
                self.load_session()
                return
            except InvalidCookieException:
                pass
        self.new_session()
    
    def load_session(self):
        try:
            self.doc = list(db().view("session/by_id", key=self.id, include_docs=True))[0].doc
        except IndexError:
            raise InvalidCookieException()
        
    def new_session(self):
        self.doc = {"type": "session", "data":{}, "date": dateutils.totuple(self.date)}
    
    def save(self):
#        if not self.changed:
#            return

        self.id, self.doc["_rev"] = db().save(self.doc)
        print self.id
    
    def get(self, *args, **kwargs):
        self.init()
        return self.doc["data"].get(*args,**kwargs)
    
    def __setitem__(self, *args, **kwargs):
        self.init()
        self.changed = True
        return self.doc["data"].__setitem__(*args,**kwargs)
    
    def set_cookie(self, response):
        if self.is_init:
            print "Jeg bliver kørt"
            response.set_cookie("session", self.id, max_age=31536000)
