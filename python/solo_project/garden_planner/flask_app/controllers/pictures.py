from flask_app import app
from flask import render_template, session, redirect, request, flash, url_for
from flask_bcrypt import Bcrypt
from flask_app.models import user
from flask_app.models import picture
bcrypt = Bcrypt(app)


@app.route('/addGardenPlan', methods=['POST'])
def addPhoto():
    if 'user_id' not in session:
        print("Not in session authorized user only!!!")
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    new_photo = {
        "picture": request.form['picture'],
        "name": request.form ['name'],
        "garden_plan": request.form ['garden_plan'],
        "users_id": request.form ['users_id']
    }
    picture.Picture.save(new_photo)  
    user.User.get_one(data)
    return redirect('/gardenPlan')
