# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, urlfor, redirect
import app.model.entries as entries


def index():
    derp = entries.getgroup(local.session.get("group"))

    herp = entries.getbalances(local.session.get("group"))
    
    template_response("/page/index.mako",
        balances = herp,
        entries = derp
    )
