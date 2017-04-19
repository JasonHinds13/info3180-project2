from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, jsonify, make_response
from flask_login import login_user, logout_user, current_user, login_required
from bs4 import BeautifulSoup
import requests
import urlparse
from forms import *
from models import *
from imageGetter import *

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route("/api/users/register", methods=["POST"])
def register():
    form = SignUpForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        password = form.password.data

        new_user = UserProfile(username=username, first_name=first_name, last_name=last_name, password=password)

        db.session.add(new_user)
        db.session.commit()

        return "Success"

@app.route("/api/users/<int:userid>/wishlist", methods=["GET","POST"])
def wishlist(userid):

    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass

@app.route('/api/thumbnails', methods=["GET"])
def thumbnails(url):
    """API for thumbnails"""

    if request.method == "GET":

        res = {"error": "null", "message": "success", "thumbnails": getImg(url)}

        response = make_response(jsonify(res))
        response.headers['Content-Type'] = 'application/json'

        return response

@app.route("/api/users/<int:userid>/wishlist/<int:itemid>", methods=["DELETE"])
def deleteitem(userid,itemid):
    pass

@app.route("/api/users/login", methods=["POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        uname = form.username.data
        pword = form.password.data

        user = UserProfile.query.filter_by(username=uname, password=pword).first()

        if user is not None:
            login_user(user)
            flash('Logged in successfully.', 'success')
            #return redirect(url_for("secure_page")) # they should be redirected to a secure-page route instead

        else:
            #flash('Username or Password is incorrect.', 'danger')
            #return

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
