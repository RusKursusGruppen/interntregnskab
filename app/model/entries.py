from app.utils.misc import db
import app.utils.date as dateutils
import app.model.user as user
import grp


class PermissionError(Exception): pass

def add(username, group, description, amount, creditor, debtors):
    date = dateutils.totuple(dateutils.now())
    
    members = set(grp.getgrnam(group).gr_mem)
    
    if not creditor in members:
        raise PermissionError()

    for debtor in debtors:
        if not debtor[0] in members:
            raise PermissionError()
    
    db().save({
        "type": "entry",
        "date": date,
        "description": description,
        "amount": amount,
        "username": username,
        "group": group,
        "creditor": creditor,
        "debtors": debtors,
    })

def getbalances(group):
    q = db().view("entry/balances",
        startkey=[group],
        endkey=[group+u"\ufff0"],
        group=True,
        reduce=True,
        group_level=2
    )
    
    for x in q:
        yield x.key[1], x.value

def getgroup(group):
    q = db().view("entry/groups",
        startkey=[group],
        endkey=[group+u"\ufff0"],
        include_docs=True,
    )

    for x in q:
        doc = x.doc

        yield {
            "id": doc.id,
            "amount": doc["amount"],
            "creditor": doc["creditor"],
            "date": dateutils.fromtuple(doc["date"]),
            "description": doc["description"],
            "debtors": dict(doc["debtors"]),
            "username": doc["username"],
        }
