'''
The below 7 lines import all of the modules necessary for the backend and backend/frontend connection. The especially important imports are the json, init, and sqlalchemy imports.
The "import json" import allows for the code in line 53, where the dump records are returned in json format, so that the python objects are readable in JSON format (text format). SQLAlchemy
is the database library being used to store all of the database info for this feature. Finally, the _init_ module is necessary, as it lets the interpreter know that there is Python code in a particular directory. 
In this case, there is Python code in the /api and /model directories.
'''

from random import randrange
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

'''
The below is where the "reviewDay" class is being defined. This contains all of the data for the feature that needs to be managed.
'''
class reviewer(db.Model):
    __tablereview__ = 'reviewTime'  
    
    '''
    The below sets all of the keys that are going to be looked at. The id key is special, as it is the primary key. This is what any sort of PUT and DELETE requests will be passed through if operable.
    '''
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), nullable=False)
    _email = db.Column(db.String(255), nullable=False)
    _reviewtx = db.Column(db.String(255), nullable=False )
    
    '''
    This is constructing the review object and the "_init_" portion is initializing the variables within that review object. 
    In this case, this is the review, email, and fun variables that are within this object.
    '''
    def __init__(self, email, reviewtx):
        self._name = name
        self._email = email
        self._reviewtx = reviewtx
    
    '''
    the following lines 44-75 contain the setter and getter methods. each of the three above variables (review, email, fun)
    are being extracted from the object and then upemaild after the object is created. 
    '''
    @property
    def name(self):
        return self._name
    
    # setting name variable in object

    @name.setter
    def name(self, name):
       self._name = name
    
    # extracting email from object
    @property
    def email(self):
        return self._email
    
    # setting email variable in object
    
    @email.setter
    def email(self, email):
       self._email = email
    
    # extracting fun from object
    
    @property
    def reviewtx(self):
        return self._reviewtx
    
    # setting fun variable in object
    
    @reviewtx.setter
    def fun(self, reviewtx):
       self._reviewtx = reviewtx
    
    '''
    The content is being outputted using "str(self)". It is being returned in JSON format, which is a readable format. This is a getter function.
    '''
    def __str__(self):
        return json.dumps(self.read())
    
    
    '''
    defining the create method. self allows us to access all of the attributes 
    of the current object. after the create method is defined, the data is queried from the DB.
    in this case, since it is the create method, the data is being ADDED, and then db.session.commit() is used
    to commit the DB transaction and apply the change to the DB.
    '''
    
    '''
    here, there is an integrity error "except" statement. db.session would be autocommitted 
    without the db.session.remove() line, and that's something we don't want for the purpose of the project.
    '''
    def create(self):
        try:
            db.session.add(self)  
            db.session.commit() 
            return self
        except IntegrityError:
            db.session.remove()
            return None
    
    '''
    the delete method is defined with the "self" parameter. this method is mainly for certain instances in the DB being 
    garbage collected, and the object kills itself.
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    '''
    read method with the self parameter, reading the object with all of the 
    properties: review, email, and fun are being returned.
    '''
    def read(self):
        return {
            "name" : self.name,
            "email" : self.email,
            "reviewtx" : self.reviewtx,
        }

'''
handling the situation where the table is completely empty,
returns the length from the session query of the initialized class reviewDay to be 0.
'''
def review_table_empty():
    return len(db.session.query(reviewer).all()) == 0
'''
defines the initreview function, and then creates the tables and the DB here through the db.create_all() method.
'''
def initreview():
    db.create_all()
    #db.init_app(app)
    if not review_table_empty():
        return
    
    r1 = reviewer('Daves Hot Chicken', '1268 Auto Park Way, Escondido, CA 92029', "8/10")
    r2 = reviewer('Raising Canes', '8223 Mira Mesa Blvd, San Diego, CA 92126', "10/10")
    r3 = reviewer('Belmont Park', '3146 Mission Blvd, San Diego, CA 92109', "7/10")
    r4 = reviewer('Potato Chip Rock', 'Ramona, CA 92065', "6/10") 
    
    '''
    the variable "reviewslist" being used for the tester data, containing a1, a2, a3, and a4 the variables with the sample data above.
    '''
    reviewslist = [r1, r2, r3, r4]
    
    
    '''
    the below is for the sample data: for each review in the defined reviewlist, the DB session will add that review, and then commit the transaction
    with the next line. or, if there is bad/duplicate data, the data will not be committed, and session will be rolled back to its previous
    state. 
    '''

    for review in reviewslist:
        try:
            db.session.add(review)
            db.session.commit()
        except IntegrityError as e:
            print("Error: " +str(e))
            '''fails with bad or duplicate data'''
            db.session.rollback()    