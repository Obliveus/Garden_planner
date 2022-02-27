from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 


class Picture:
    db = 'vegetables'
    def __init__(self,data):
        self.id = data['id']
        self.picture = data['picture']
        self.name = data['name']
        self.garden_plan = data['garden_plan']
        

# saves the new picture
    @classmethod
    def save(cls,data):
            query = "INSERT INTO pictures (picture, name, garden_plan, users_id) VALUES(%(picture)s, %(name)s, %(garden_plan)s, %(users_id)s)"
            return connectToMySQL(cls.db).query_db(query,data)

# shows all pictures
    @classmethod
    def allPictures(cls):
            query = "SELECT * FROM pictures;"
            results = connectToMySQL(cls.db).query_db(query)
            pictures = []
            for picture in results:
                pictures.append(cls(picture))
            return pictures

# Shows one picture
    @classmethod
    def onePicture(cls,data):
            query = "SELECT * FROM pictures WHERE id = %(id)s;"
            results = connectToMySQL(cls.db).query_db(query,data)
            if len(results) < 1:
                return False
            return cls(results[0])

# Shows pictures associated with a user
    @classmethod
    def get_pictures_by_user(cls,data):
            query = "SELECT * FROM users LEFT JOIN pictures on pictures.users_id = users.id WHERE users.id = %(id)s;"
            results = connectToMySQL(cls.db).query_db(query,data)
            if len(results) < 1:
                return False
            return Picture(results[0])

# Updates the picture
    @classmethod
    def update(cls, data):
        query = 'UPDATE pictures SET picture=%(picture)s, name=%(name)s, garden_plan=%(garden_plan)s WHERE pictures.id=%(id)s;'
        return connectToMySQL(cls.db).query_db(query, data)

        
# Deletes picture
    @classmethod
    def delete(cls, data):
            query = 'DELETE FROM pictures WHERE id = %(id)s;'
            return connectToMySQL(cls.db).query_db(query, data)
