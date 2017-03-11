from database import Database
from user import User
Database.initialize(user = 'postgres', password = 'Mukhtar1', database = 'learning', host = 'localhost')

user = User('rolf_smith@yahoo.com', 'Rolf', 'Smith', None)
user.SaveToDB()

user_from_database = User.load_from_db_email('shahedaafroza@yahoo.com')
print(user_from_database)
