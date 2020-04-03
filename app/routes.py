from flask import render_template, flash, redirect, url_for, request, abort
from werkzeug.urls import url_parse
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
        flash('Successfully created link ' + link.slug + '!')
        return redirect(url_for('index', slug=bot.slug))
    return render_template('index.html',
                           title='Create new link',
                           form=form)


