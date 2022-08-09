# Importamos la clase de nuestro archivo de conexion
from crud_app.config.mysqlconnection import connectToMySQL


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.email=data['email']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, form):
        query = "INSERT INTO users (first_name,last_name,email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        
        result = connectToMySQL('crud').query_db(query,form);
        
        return result

    @classmethod
    def show_user(cls, form):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('crud').query_db(query,form)
        print(result)
        return cls(result[0])


    @classmethod
    def show_users(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL('crud').query_db(query)
        users = []
        for u in result:
            instance_user = cls(u)
            users.append(instance_user)
        return users
    
    @classmethod
    def update_user(cls, form):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('crud').query_db(query,form)

    @classmethod
    def delete_user(cls, form):
        query = "DELETE FROM users WHERE id = %(id)s;"
        result = connectToMySQL('crud').query_db(query,form)
        return result
