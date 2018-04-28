from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    phone = StringField('手机号：', validators= [DataRequired() ,Length(1,14)])
    password = PasswordField('密码：' , validators=[DataRequired()])
    submit = SubmitField('登录')