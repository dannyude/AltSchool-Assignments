import os
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo


# Load country data
def load_country_data():
    file_path = os.path.join(os.path.dirname(__file__), "countries.json")
    with open("countries.json") as f:
        countries = json.load(f)
    return [(country["code"], country["name"]) for country in countries]


class SignupForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    gender = SelectField(
        "Gender",
        choices=[("male", "Male"), ("female", "Female")],
        validators=[DataRequired()],
    )
    date_of_birth = DateField(
        "Date of Birth (dd/mm/yyyy)", format="%d/%m/%Y", validators=[DataRequired()]
    )
    email_address = StringField("Email Address", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    country = SelectField(
        "Select your country",
        choices=load_country_data(),
        validators=[DataRequired()],
    )
    city = StringField("City", validators=[DataRequired()])
    how_heard = StringField("How did you hear about us?")
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
    )
