from app import app, db


class Link(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String)
    redirect_url = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    subtext = db.Column(db.String)
    image_url = db.Column(db.String)
    favicon_url = db.Column(db.String)
