from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL


class LinkForm(FlaskForm):
    redirect_url = StringField('URL to redirect to', validators=[DataRequired(), URL()])
    title = StringField('Fake page title', validators=[DataRequired()])
    subtext = StringField('Page subtext (optional)')
    image_url = StringField('Splash image URL (optional)', validators=[URL()])
    favicon_url = StringField('URL of fake favicon (optional)', validators=[URL()])

    submit = SubmitField('Submit')
