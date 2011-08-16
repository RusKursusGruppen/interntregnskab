# -*- coding: utf-8 -*-
import app.utils.misc

def timedelta(date):
    return app.utils.misc.template_render('/widget/timedelta.mako', date=date)

def currentuser():
    import app.model.user
    return app.model.user.getname(app.utils.misc.local.session.get("uid"))

def currentgroup():
    import app.model.user
    return app.model.user.getgroup(app.utils.misc.local.session.get("uid"))
