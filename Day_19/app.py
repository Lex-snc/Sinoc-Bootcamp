from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from extensions import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sample_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    age = request.form.get('age')
    address = request.form.get('address')
    bday = request.form.get('bday')
    
    if confirm_password != password:
        flash('Passwords do not match!')
        return redirect(url_for('register'))

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password, confirm_password=confirm_password, fname=fname, lname=lname, age=age, address=address, bday=bday)

    try: 
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful!")
    except Exception as e:
        db.session.rollback()
        flash(f"Error occurred: {str(e)}")
        return redirect(url_for('home'))

    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Query the user from the database
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        flash("Login successful!")
        return render_template('home.html', result=user)
    else:
        flash("Invalid email or password")
        return render_template('home.html')

@app.route('/add-info', methods=['POST'])
def add_info():
    email = request.form.get('email')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    age = request.form.get('age')
    address = request.form.get('address')
    bday = request.form.get('bday')

    # Find user by email
    user = User.query.filter_by(email=email).first()

    if user:
        # Update user info
        user.fname = fname
        user.lname = lname
        user.age = age
        user.address = address
        user.bday = bday

        try:
            db.session.commit()
            flash('Information updated successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating info: {e}')
    else:
        flash('User not found.')

    return render_template('home.html', fname=fname, lname=lname, age=age, address=address, bday=bday)



# Setup Flask-Admin
admin = Admin(app, name='SQLite Admin', template_mode='bootstrap4')
admin.add_view(ModelView(User, db.session))

if __name__ == '__main__':
    app.run(debug=True)
