# Database related imports
# Make sure to import your tables!
from model import Base, Student

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

def add_Flavor(name, ingridents):
    print("Added a flavor!")
    new_ice_cream = Flavor(name=flavor_name, ingrients=flavor_ingridents)
    session.add(new_ice_cream)
    session.commit()

def add_user(name,email):
    """Add a user to the DB."""
    user = User(username=name, email_address=email)
    session.add(user)
    session.commit()

def get_all_flavors():
    ice_cream = session.query(Flavor).all()
    return ice_cream