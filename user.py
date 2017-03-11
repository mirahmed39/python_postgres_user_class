# the user class creates user objects and for each instance
# it stores the the user's first name, last name and email address
# The class also provides methods to save and load user instance from database.

from database import CursorFromConnectionFromPool

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "User: {} {}".format(self.last_name, self.first_name)

    def SaveToDB(self):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)', (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            user_data = cursor.fetchone()
            return cls(user_data[1], user_data[2], user_data[3], user_data[0])

