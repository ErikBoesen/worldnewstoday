from app import app, db


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    redirect_url = db.Column(db.String, required=True)
    title = db.Column(db.String, required=True)
    subtext = db.Column(db.String)
    image_url = db.Column(db.String)
    favicon_url = db.Column(db.String)
