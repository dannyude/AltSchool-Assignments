from flask import render_template, url_for
from flaskr import app
from flaskr.forms import SignupForm
from flaskr.forms import load_country_data


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/sign_up")
def sign_up():
    form = SignupForm()
    countries = load_country_data()
    return render_template(
        "sign_up.html", title="sign up", form=form, countries=countries
    )


@app.route("/about_me")
def about_me():
    return render_template("about_me.html", title="About me")
