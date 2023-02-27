from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

class reviewadd(db.Model):
    __tablename__ = 'reviewEnter'  
    
    id = db.Column(db.Integer, primary_key=True)
    _reviewtx = db.Column(db.String(255), nullable=False)
    _email = db.Column(db.String(255), nullable=False)
    _star = db.Column(db.String(255), nullable=False )
    
    def __init__(self, reviewtx, email, star):
        self._reviewtx = reviewtx
        self._email = email
        self._star = star
        
    @property
    def reviewtx(self):
        return self._reviewtx
    
    @reviewtx.setter
    def fact(self, reviewtx):
       self._reviewtx = reviewtx
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
       self._email = email
    
    @property
    def star(self):
        return self._star
    
    @star.setter
    def star(self, star):
       self._star = star
    
    def __str__(self):
        return json.dumps(self.read())

    def create(self):
        try:
            db.session.add(self)  
            db.session.commit() 
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
    
    def read(self):
        return {
            "reviewtx" : self.reviewtx,
            "email" : self.email,
            "star" : self.star
        }
        
def details_table_empty():
    return len(db.session.query(reviewadd).all()) == 0

def initreviewpost():
    # db.create_all()
    db.init_app(app)
    if not details_table_empty():
        return
    
    print("Creating test data")
    """Create database and tables"""
    """Tester data for table"""
    
    r1 = reviewadd(reviewtx="This was a good vacation spot", star="four", email="hiphop@gmail.com")
    r2 = reviewadd(reviewtx="This was a good website and I had a good time", star="five", email="vacationers@gmail.com")
    r3 = reviewadd(reviewtx="I really recommend this to everyone it was fun", star="four", email="billybob@gmail.com")

    
    reviewpick = [r1, r2, r3]
    

    for review in reviewpick:
        try:
            db.session.add(review)
            db.session.commit()
        except IntegrityError as e:
            print("Error: " +str(e))
            '''fails with bad or duplicate data'''
            db.session.rollback()

initreviewpost()
    