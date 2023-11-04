from flask import Flask
from flask import render_template, request
from forms import LoginForm, RegistrationForm
from flask_wtf.csrf import CSRFProtect
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        print(email, password, name)
        user = User(name=name, email=email, password=password)
        db.create_all()
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
