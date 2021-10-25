from app import db
# file needs access to the SQLAlchemy db

class Book(db.Model):
    # inherit db.Model class
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    # creates title attribute which maps to a string cloumn 'title'
    description = db.Column(db.String)
    # creates description attribute which will map to a string column 'description'