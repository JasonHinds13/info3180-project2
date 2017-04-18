from . import db

class WishListItem(db.Model):
    itemid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    website = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))
