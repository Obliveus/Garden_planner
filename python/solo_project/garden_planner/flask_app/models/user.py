from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import vegetable
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db = 'vegetables'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.vegetablesList = []
        
    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query, user)
        print(len(results))
        if len(results) > 0:
            flash("Email already taken.", "register")
            is_valid = False
        if len(user['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 3 characters.","register")
        if len(user['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 3 characters.","register")
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Invalid Email Address.","register")
        if len(user['email']) < 8:
            flash("Email already taken.", "login")
            is_valid = False    
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.","register")
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Passwords do not match!","register")
        return is_valid


    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name, email ,password, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return User(results[0]) 

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def userVegetables(cls, data):
        query = 'SELECT * FROM users LEFT JOIN vegetables ON vegetables.users_id = users.id WHERE users.id = %(id)s;'
        results = connectToMySQL(cls.db).query_db(query, data)
        print("User Vegetable query results: ", results)
        listOfVegetables = cls(results[0])
        for row in results:
            data = {
                'id': row['vegetables.id'],
                'vegetable': row['vegetable'],
                'zone': row['zone'],
                'planting_date': row['planting_date'],
                'harvest_date': row['harvest_date'],
                'users_id': row['users_id']
            }
            items = vegetable.Vegetable(data)
            print("Each item: ", items)
            listOfVegetables.vegetablesList.append(items)
        return listOfVegetables

    @classmethod
    def gardenPlan(cls, data):
        query = "SELECT garden_plan FROM pictures WHERE id = %(id)s AND users.id = user_id;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])