from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Vegetable:
    db = 'vegetables'
    def __init__(self,data):
        self.id = data['id']
        self.vegetable = data['vegetable']
        self.zone = data['zone']
        self.planting_date = data['planting_date']
        self.harvest_date = data['harvest_date']
        
    # Validates the vegetable
    @staticmethod
    def validate_vegetables(vegetable):
        isvalid = True
        query = "SELECT * FROM vegetables;"
        results = connectToMySQL(Vegetable.db).query_db(query, vegetable)
        print(len(results))
        if len(vegetable['vegetable']) < 2:
            isvalid = False
            flash("Vegetable name must be more than two characters.","vegetable")
        if len(vegetable['zone']) < 1:
            isvalid = False
            flash("Zone not entered","vegetable")
        if len(vegetable['planting_date']) < 2:
            isvalid = False
            flash("The vegetable planting date is missing.","vegetable")    
        if len(vegetable['harvest_date']) < 2:
            isvalid = False
            flash("The vegetable harvest date is missing.","vegetable")   
        return isvalid

# saves the new vegetable
    @classmethod
    def save(cls,data):
            query = "INSERT INTO vegetables (vegetable, zone, planting_date, harvest_date, users_id) VALUES(%(vegetable)s, %(zone)s, %(planting_date)s, %(harvest_date)s, %(users_id)s)"
            return connectToMySQL(cls.db).query_db(query,data)

# shows all vegetables
    @classmethod
    def allVegetables(cls):
            query = "SELECT * FROM vegetables;"
            results = connectToMySQL(cls.db).query_db(query)
            vegetables = []
            for vegetable in results:
                vegetables.append(cls(vegetable))
            return vegetables

# Shows one vegetable
    @classmethod
    def oneVegetable(cls,data):
            query = "SELECT * FROM vegetables WHERE id = %(id)s;"
            results = connectToMySQL(cls.db).query_db(query,data)
            if len(results) < 1:
                return False
            return cls(results[0])

# Shows vegetables associated with a user
    @classmethod
    def get_vegetables_by_user(cls,data):
            query = "SELECT * FROM users LEFT JOIN vegetables on vegetables.users_id = users.id WHERE users.id = %(id)s;"
            results = connectToMySQL(cls.db).query_db(query,data)
            if len(results) < 1:
                return False
            return Vegetable(results[0])

# Updates the vegetable
    @classmethod
    def update(cls, data):
        query = 'UPDATE vegetables SET vegetable=%(vegetable)s, zone=%(zone)s, planting_date=%(planting_date)s, harvest_date=%(harvest_date)s WHERE vegetables.id=%(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

        
# Deletes vegetable
    @classmethod
    def delete(cls, data):
            query = 'DELETE FROM vegetables WHERE id = %(id)s;'
            return connectToMySQL(cls.db).query_db(query, data)

# Joins the selected columns from the two tables.
    @classmethod
    def userAndVegetables(cls):
        query = 'SELECT vegetable, users_id, first_name, vegetables.id FROM vegetables LEFT JOIN users ON vegetables.users_id = users.id;'
        results = connectToMySQL(cls.db).query_db(query)
        print("User vegetable query results: ", results)
        users = []
        for user in results:
            users.append(user)
        print("This is users", users)            
        return users