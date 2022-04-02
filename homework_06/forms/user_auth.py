from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Regexp, Email, EqualTo, ValidationError
from homework_06.models.all_models import User


class UserRegistrationForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(5, 20),
            Regexp(
                '^[a-zA-Z]+[a-zA-Z0-9_.]*$',
                0,
                'Имя пользователя должно содержать только буквы латинского алфавита, цифры точки и подчеркивания'
            )
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(5, 30)])
    password1 = PasswordField(validators=[InputRequired(), Length(8, 50)])
    password2 = PasswordField(
        validators=[
            InputRequired(),
            Length(8, 50),
            EqualTo('password1', message='Пароли не совпадают')
        ]
    )
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Пользователь с такой электронной почтой уже существует')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Пользователь с таким именем уже существует')


class UserLoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email(), Length(5, 30)])
    password = PasswordField(validators=[InputRequired(), Length(8, 50)])
    submit = SubmitField('Войти')

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append('Неверные пароль или email')
