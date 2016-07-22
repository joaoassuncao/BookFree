from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)


# Login

    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    
#Info

    name = db.Column(db.String)
    cpf = db.Column(db.String)
    gender = db.Column(db.String)
    birthday = db.Column(db.Date) 
    
    def __repr__(self):
        return "<User %r>" % self.email
        
class Book(db.Model):
    id = db.Column(db.Integer, primary_key  = True)
    
    #Info
    title = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    publisher = db.Column(db.String, nullable = False)
    gender = db.Column(db.String, nullable = False)
    isbn = db.Column(db.String)
    
    def __repr__(self):
        return "<Book %r>" % self.title

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    #Info
    id_lender = db.Column(db.Integer, nullable = False)
    id_borrower = db.Column(db.Integer, nullable = False)
    id_book  = db.Column(db.Integer, nullable = False)
    