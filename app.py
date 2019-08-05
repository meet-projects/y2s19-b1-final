# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_Flavor, add_user, get_all_flavors

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')
def create_flavor():
	return render_template("create_flavor.html")

@app.route('/vote')
def vote():
	return render_template('voting.html')












# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
