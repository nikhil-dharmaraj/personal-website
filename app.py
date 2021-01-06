import os
from tempfile import mkdtemp
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Route for the intro page.
@app.route("/")
def homepage():
    """Show introduction page"""
    return render_template("home.html")

#Route for the about page.
@app.route("/about")
def about():
    """Show about page"""
    return render_template("about.html")

#Route for the portfolio page.
@app.route("/portfolio")
def portfolio():
    """Show portfolio page"""
    return render_template("portfolio.html")

#Route for the contact page.
@app.route("/contact")
def contact():
    """Show contact page"""
    return render_template("contact.html")