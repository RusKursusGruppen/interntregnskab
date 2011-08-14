# -*- coding: utf-8 -*-
import app.utils.misc

def timedelta(date):
    return app.utils.misc.template_render('/widget/timedelta.mako', date=date)

