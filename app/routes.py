from flask import render_template, redirect, url_for
from app import app, db
from app.forms import LinkForm
from app.models import Link


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    if form.validate_on_submit():
        link = Link(redirect_url=form.redirect_url.data,
                    title=form.title.data,
                    subtext=form.subtext.data,
                    image_url=form.image_url.data,
                    favicon_url=form.favicon_url.data)
        link.slug = '-'.join(link.title.lower().split()[:8])
        db.session.add(link)
        db.session.commit()
        return render_template('index.html',
                                url=url_for('do_redirect', _external=True, slug=link.slug))
    return render_template('index.html',
                           form=form)


@app.route('/article/<slug>')
def do_redirect(slug):
    link = Link.query.filter_by(slug=slug).first_or_404()
    db.session.close()
    return render_template('redirect.html', link=link)
