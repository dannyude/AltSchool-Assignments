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


@app.route("/engineering")
def engineering():
    return render_template("pages/engineering.html", title="Engineering")


@app.route("/product")
def product():
    return render_template("pages/product.html", title="Product")


@app.route("/data")
def data():
    return render_template("pages/data.html", title="Data")


@app.route("/business")
def business():
    return render_template("pages/business.html", title="Business")


@app.route("/creative_economy")
def creative_economy():
    return render_template("pages/creative_economy.html", title="Creative Economy")


@app.route("/about_me")
def about_me():
    return render_template("about_me.html", title="About me")


@app.route("/media")
def media():
    return render_template("pages/media.html", title="Anime Journey")
