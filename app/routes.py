from flask import render_template, redirect, url_for, abort
from app import app, db
from app.forms import LinkForm
from app.models import Link


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    if form.validate_on_submit():
        link = Link(redirect_url=form.url_redirect.data,
                    title=form.title.data,
                    subtext=form.subtext.data,
                    image_url=form.image_url.data,
                    favicon_url=form.favicon_url.data,

        db.session.add(link)
        db.session.commit()
        return redirect(url_for('index', slug=bot.slug))
    return render_template('index.html',
                           title='Create new link',
                           form=form)


