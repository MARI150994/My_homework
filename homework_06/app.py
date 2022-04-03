from os import getenv

from flask import Flask, render_template, url_for, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from flask_migrate import Migrate
from itsdangerous import URLSafeTimedSerializer, BadData

from forms.user_auth import UserLoginForm, UserRegistrationForm
from models.database import db
from models import User
from views.places import places_app

app = Flask(__name__)
CONFIG_OBJECT_PATH = "config.{}".format(getenv("CONFIG_NAME", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJECT_PATH)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)

app.register_blueprint(places_app, url_prefix="/places")

token_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = UserRegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        user = User(username=username, email=email)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        # generate token for confirmation
        token = token_serializer.dumps(user.email, salt=app.config['SALT'])
        conf_url = url_for('confirm_url', token=token, _external=True)
        # prepare data to send
        message = Message(
            subject='Активация акканута',
            body=f'Для активации акканута пройдите по ссылке: {conf_url}',
            recipients=[user.email],
            sender=app.config['MAIL_DEFAULT_SENDER'],
        )
        mail.send(message)
        login_user(user)
        return render_template('auth/confirm_user.html', message='Для подтверждения аккаута пройдите по ссылке в почте')
    return render_template('auth/register.html', form=form)


@app.get('/confirm')
def confirm_user():
    if current_user.confirmed:
        return redirect('index')
    return render_template('auth/confirm_user.html')


@app.route('/confirm/<token>')
@login_required
def confirm_url(token):
    # check token
    try:
        email = token_serializer.loads(token, salt=app.config['SALT'], max_age=3600)
    except BadData:
        return render_template('auth/confirm_user.html', message='Ссылка не активна')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        return render_template('auth/confirm_user.html', message='Ваш аккаунт уже активирован')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        return render_template('auth/confirm_user.html', message='Вы активировали аккаунт')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('auth/login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.get('/')
def index():
    return render_template('index.html')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
