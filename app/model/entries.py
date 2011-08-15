from app.utils.misc import db
import app.utils.date as dateutils
import app.model.user as user
import grp


class PermissionError(Exception): pass

def add(author, group, amount, creditor, debtors):
    date = dateutils.totuple(dateutils.now())
    
    members = set(grp.getgrnam(group).gr_mem)
    
    if not creditor in members:
        raise PermissionError()

    for username in debtors:
        if not username in members:
            raise PermissionError()
    
    db().save({
        "type": "entry",
        "date": date,
        "amount": amount,
        "author": author,
        "group": group,
        "creditor": creditor,
        "debtors": debtors,
    })
