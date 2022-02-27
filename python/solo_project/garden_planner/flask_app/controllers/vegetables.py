from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
from flask_app.models import vegetable
from flask_app.models import picture

bcrypt = Bcrypt(app)

@app.route('/addVeggies')
def addVeggies():
    if 'user_id' not in session:
        print("Not in session authorized user only!!!")
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    users=user.User.get_one(data)
    return render_template("addVeggies.html", users=users)

@app.route('/veggies')
def allveggies():
    vegetables=vegetable.Vegetable.allVegetables()
    usersVegetables=vegetable.Vegetable.userAndVegetables()
    return render_template("____.html", usersVegetables=usersVegetables, vegetables=vegetables)

@app.route('/createVeggie', methods=['POST'])
def create():
    isvalid = vegetable.Vegetable.validate_vegetables(request.form)
    if not isvalid:
        return redirect("/addVeggies")

    new_vegetable = {
        "vegetable": request.form["vegetable"],
        "planting_date": request.form ["planting_date"],
        "harvest_date": request.form ["harvest_date"],
        "zone": request.form ["zone"],
        "users_id": request.form ["users_id"]
    }
    vegetable.Vegetable.save(new_vegetable)  
    return redirect('/home')


@app.route('/edit/<int:vegetables_id>')
def edit(vegetables_id):
    vegetables_id = {
        'id': vegetables_id
    }
    data = {
        "id": session['user_id']
    }

    oneVegetable = vegetable.Vegetable.oneVegetable(vegetables_id)
    users=user.User.get_one(data)
    return render_template("edit.html", users=users, oneVegetable=oneVegetable)
    
@app.route('/update/', methods=['POST'])
def update():
    updateVegetable = {
        "vegetable": request.form["vegetable"],
        "planting_date": request.form ["planting_date"],
        "harvest_date": request.form ["harvest_date"],
        "zone": request.form ["zone"],
        "id": request.form ["vegetables_id"]
    }
    vegetable.Vegetable.update(updateVegetable)
    return redirect('/home')

@app.route('/delete/<int:vegetables_id>')
def deletedVegetable(vegetables_id):
    data = {
        'id': vegetables_id
    }
    vegetable.Vegetable.delete(data)
    return redirect('/home')
