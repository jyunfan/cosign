from google.appengine.ext import db

class Sign(db.Model):
    count = db.IntegerProperty(indexed=True)
    date  = db.DateProperty(indexed=False)
    name  = db.StringProperty(indexed=False)
    birth = db.DateProperty(indexed=False)
    addr  = db.StringProperty(indexed=False)
    phone = db.StringProperty(indexed=False)

class Counter(db.Model):
    count = db.IntegerProperty(indexed=False)

