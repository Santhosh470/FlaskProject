from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username",validators = [DataRequired(), Length(min= 2, max = 20)])
    email = StringField("Email",validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password", message="passwords must match")])
    submit = SubmitField("Sign up")
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("That username is already taken.")
    def validate_email(self, email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError("That email has already been registered")

class LoginForm(FlaskForm):
    #username = StringField("Username",validators = [DataRequired(), Length(min= 2, max = 20)])
    email = StringField("Email",validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("Login")
    remember = BooleanField("remember me")

class UpdateAccountForm(FlaskForm):
    username = StringField("Username",validators = [DataRequired(), Length(min= 2, max = 20)])
    email = StringField("Email",validators = [DataRequired(), Email()])
    submit = SubmitField("Update")
    picture = FileField("Update profile picture", validators=[FileAllowed(["jpg", "png"])])
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError("That username is already taken.")
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email = email.data).first()
            if email:
                raise ValidationError("That email has already been registered")

class RequestResetForm(FlaskForm):
    email = StringField("Email",validators = [DataRequired(), Email()])
    submit = SubmitField("Request Password reset")
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email you must register first")

class ResetPasswordForm(FlaskForm):
    password = PasswordField("New Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password", message="Passwords must match")])
    submit = SubmitField("Reset Password")