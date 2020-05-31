from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,  ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min =2, max = 20)])
    #data required= it cant be empty and length of btw 2 and 20, stringfield holds the labels
    email = StringField("Email",validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

#template-to to validate field def validate_field(self,field): if true raise ValidationError
    def validate_username(self,username):
        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken! Please choose another one")
    def validate_email(self,email):
        user= User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken! Please choose another one")


class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")

class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min =2, max = 20)])
    #data required= it cant be empty and length of btw 2 and 20, stringfield holds the labels
    email = StringField("Email",validators=[DataRequired(), Email()])
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]) #can add more file extensions
    submit = SubmitField("Update")

#template-to to validate field def validate_field(self,field): if true raise ValidationError
    def validate_username(self,username):
        if username.data!= current_user.username:
            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That username is taken! Please choose another one")
    def validate_email(self,email):
        if email.data!= current_user.email:
            user= User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("That email is taken! Please choose another one")

class RequestResetForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(), Email()])
    submit = SubmitField("Request Password Reset")
    def validate_email(self,email):
        user= User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email. Kindly register.")

class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Reset Password")
