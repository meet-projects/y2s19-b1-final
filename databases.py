# Database related imports
# Make sure to import your tables!
from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

def add_Flavor(name, add_ons, flavor):
    print("Added a flavor!")
    new_ice_cream = Flavor(name=name, add_ons=add_ons, flavor=flavor)
    session.add(new_ice_cream)
    session.commit()
    return new_ice_cream.id

def add_user(name,email, flavor_id):
    """Add a user to the DB."""
    print("+++" + str(flavor_id))
    user = User(username=name, email=email, flavor_id=flavor_id)
    session.add(user)
    session.commit()

def get_all_flavors():
    ice_cream = session.query(Flavor).all()
    return ice_cream

def submit_option(option,user_email):
    vote = Vote(option=option, user_email=user_email)
    session.add(vote)
    session.commit()