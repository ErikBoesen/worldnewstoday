from app import app, db


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, required=True)
    subtext = db.Column(db.String)
    image_url = db.Column(db.String)
    redirect_url = db.Column(db.String, required=True)
