# Database related imports
# Make sure to import your tables!
from model import Base, User, Flavor

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

def add_Flavor(name, add_ons, ice_cream_flavor, user_id):
    print("Added a flavor!")
    new_ice_cream = Flavor(name=name, add_ons=add_ons, ice_cream_flavor=ice_cream_flavor)
    session.add(new_ice_cream)
    session.commit()

def add_user(name,email, flavor_id):
    """Add a user to the DB."""
    user = User(username=name, email_address=email, flavor_id=flavor_id)
    session.add(user)
    session.commit()

def get_all_flavors():
    ice_cream = session.query(Flavor).all()
    return ice_cream