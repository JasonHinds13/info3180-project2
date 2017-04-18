from app import app
from flask import render_template, request, redirect, url_for, jsonify, make_response
from bs4 import BeautifulSoup
import requests
import urlparse
from imageGetter import *

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route("/api/users/register", methods=["POST"])
def register():
    pass

@app.route("/api/users/login", methods=["POST"])
def login():
    pass

@app.route("/api/users/<int:userid>/wishlist", methods=["GET","POST"])
def wishlist(userid):

    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass

@app.route('/api/thumbnails', methods=["GET"])
def thumbnails():
    """API for thumbnails"""

    if request.method == "GET":

        res = {"error": "null", "message": "success", "thumbnails": getImg()}

        response = make_response(jsonify(res))
        response.headers['Content-Type'] = 'application/json'

        return response

@app.route("/api/users/<int:userid>/wishlist/<int:itemid>", methods=["DELETE"])
def deleteitem(userid,itemid):
    pass

###
# The functions below should be applicable to all Flask apps.
###

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
