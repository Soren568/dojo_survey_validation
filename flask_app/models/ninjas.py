from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
DB = "dojo_survey_schema"

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas(name, location, language, comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        result = connectToMySQL(DB).query_db(query)
        ninjas = []
        for user in result:
            ninjas.append(cls(user))
        return ninjas

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True
        if len(ninja['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if ninja['location'] == "Select your location":
            flash("Please select a location")
            is_valid = False
        if ninja['language'] == "Select your favorite language":
            flash("Please select a language.")
            is_valid = False
        if len(ninja['comment']) < 3:
            flash("Comment is required. Atleast 3 characters.")
            is_valid = False
        return is_valid