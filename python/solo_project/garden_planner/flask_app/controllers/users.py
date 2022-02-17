from flask_app import app
from flask import render_template, session, redirect, request, flash
import re
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.vegetable import Vegetable

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register',methods=['POST'])
def register():
    is_valid = User.validate_user(request.form)
    if not is_valid:
        return redirect("/")

    new_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    User.save(new_user)  
    return redirect('/')


@app.route("/login",methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email","login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect("/")    
    session['user_id'] = user.id
    return redirect('/home')
    

@app.route("/home")
def home():
    if 'user_id' not in session:
        print("Not in session authorized user only!!!")
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    users = User.get_one(data)
    usersVegetables = User.userVegetables(data)
    return render_template("home.html", users=users, userVegetables=usersVegetables)

@app.route("/garden-plan")
def gardenPlan():
    if 'user_id' not in session:
        print("Not in session authorized user only!!!")
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    users = User.get_one(data)
    usersVegetables = User.userVegetables(data)
    return render_template("gardenPlan.html", users=users, userVegetables=usersVegetables)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# POSSIBLE DELETE ACCOUNT BUTTON IN ACCOUNT SETTINGS***********
@app.route('/user/<int:user_id>/delete/')
def deleteUser(users_id):
    data = {
        'id': users_id
    }
    return redirect('/', User.delete(data))