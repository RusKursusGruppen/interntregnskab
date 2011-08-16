from app.utils.misc import db
import app.utils.date as dateutils
import app.model.user as user

class PermissionError(Exception): pass

def add(uid, group, description, amount, creditor, debtors):
    date = dateutils.totuple(dateutils.now())
    
    members = set(x[0] for x in user.getmembers(uid))

    if not creditor in members:
        raise PermissionError()

    for debtor in debtors:
        if not debtor[0] in members:
            raise PermissionError()

    db().save({
        "type": "entry",
        "amount": amount,
        "creditor": creditor,
        "date": date,
        "debtors": debtors,
        "description": description,
        "group": group,
        "uid": uid,
    })

def getbalances(uid):
    group = user.getgroup(uid)
    q = db().view("entry/balances",
        startkey=[group],
        endkey=[group+u"\ufff0"],
        group=True,
        reduce=True,
        group_level=2
    )
    
    for x in q:
        yield user.getname(x.key[1]), x.value

def getgroup(uid):
    group = user.getgroup(uid)
    q = db().view("entry/groups",
        startkey=[group+u"\ufff0"],
        endkey=[group],
        include_docs=True,
        descending=True
    )

    for x in q:
        doc = x.doc
        username = user.getname(doc["uid"])
        debtors = doc["debtors"]
        debtors = dict((user.getname(x),y) for x,y in debtors)
        
        creditor = user.getname(doc["creditor"])

        yield {
            "id": doc.id,
            "amount": doc["amount"],
            "creditor": creditor,
            "date": dateutils.fromtuple(doc["date"]),
            "description": doc["description"],
            "debtors": debtors,
            "username": username,
        }
