# -*- coding: utf-8 -*-
from app.utils.misc import db
import app.utils.date as dateutils


class InvalidCookieException(Exception):
    pass

class Session(object):
    def __init__(self, id, expires):
        self.id = id
        self.is_init = False
        self.expires = expires
    
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
            doc = list(db().view("session/by_id", key=self.id, include_docs=True))[0].doc
        except IndexError:
            raise InvalidCookieException()

        # Expire time on session
        if (dateutils.now() - dateutils.fromtuple(doc["date"])).total_seconds() > self.expires:
            raise InvalidCookieException()
        
        doc["date"] = dateutils.totuple(self.date)
        self.doc = doc
        
    def new_session(self):
        self.doc = {"type": "session", "data":{}, "date": dateutils.totuple(self.date)}
    
    def save(self):
        self.id, self.doc["_rev"] = db().save(self.doc)
    
    def get(self, *args, **kwargs):
        self.init()
        return self.doc["data"].get(*args,**kwargs)
    
    def __setitem__(self, *args, **kwargs):
        self.init()
        return self.doc["data"].__setitem__(*args,**kwargs)
    
    def set_cookie(self, response):
        if self.is_init:
            response.set_cookie("session", self.id, max_age=31536000)
