from werkzeug.security import generate_password_hash # generates a unique password hash for extra security 
from flask_sqlalchemy import SQLAlchemy # this is our ORM (Object Relational Mapper)
from flask_login import UserMixin, LoginManager # helping us load a user as our current_user 
from datetime import datetime # puts a timestamp on any data we create (Users, Workouts, etc..)
import uuid # makes a unique id for our data (primary key)
from flask_marshmallow import Marshmallow


#  internal imports




# instantiate all our classes
db = SQLAlchemy() # makes database object
login_manager = LoginManager() # makes login object 
ma = Marshmallow() #makes marshmallow object

# use login_manager object to create a user_loader function
@login_manager.user_loader
def load_user(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve

    """
    return User.query.get(user_id) # this is a basic query inside our database to bring back a specific User object

# think of these as admin (keeping track of what workouts are available)
class User(db.Model, UserMixin): 
    # CREATE TABLE User, all the columns we create
    user_id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow) # this grabs a timestamp as soon as a User object is instantiated


    # INSERT INTO User() Values()
    def __init__(self, username, email, password, first_name="", last_name=""):
        self.user_id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email 
        self.password = self.set_password(password) 



    # methods for editing our attributes 
    def set_id(self):
        return str(uuid.uuid4()) # all this is doing is creating a unique identification token
    

    def get_id(self):
        return str(self.user_id) # UserMixin using this method to grab the user_id on the object logged in
    
    
    def set_password(self, password):
        return generate_password_hash(password) # hashes the password so it is secure (aka no one can see it)
    

    def __repr__(self):
        return f"<User: {self.username}>"
    
    exercises = db.relationship('Exercise', backref='user', lazy=True, cascade='all, delete-orphan')

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body_part = db.Column(db.String(50))
    equipment = db.Column(db.String(50))
    gif_url = db.Column(db.String)
    name = db.Column(db.String(100))
    target = db.Column(db.String(50))
    sets = db.Column(db.Integer, nullable=False)
    repetitions = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey("user.user_id"), nullable=False)

    def __init__(self, id, body_part, equipment, name, target, sets, repetitions, user_id, gif_url=""):
        self.id = id
        self.body_part = body_part
        self.equipment = equipment
        self.gif_url = gif_url
        self.name = name
        self.target = target
        self.sets = sets
        self.repetitions = repetitions
        self.user_id = user_id

    








# creating our Schema class (Schema essentially just means what our data "looks" like, and our 
# data needs to look like a dictionary (json) not an object)


class ExerciseSchema(ma.Schema):

    class Meta:
        fields = ['exercise_id', 'body_part', 'equipment', 'name', 'target', 'sets', 'repetitions', 'gif_url', ]



# # instantiate our ExerciseSchema class so we can use them in our application
exercise_schema = ExerciseSchema() # this is 1 singular exercise
exercises_schema = ExerciseSchema(many=True) # bringing back all the exercises in our database & sending to frontend