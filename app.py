9# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import *

# Starting the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"
# App routing code here
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/new_flavor', methods= ['GET', 'POST'])
def create_flavor():
	if request.method == "POST":
		session['flavor_id'] = add_Flavor(request.form['name'],request.form['flavor'],request.form['add_on'])
		return render_template('submit_flavor.html')
	return render_template("create_flavor1.html")

@app.route('/submit_flavor', methods= ['GET', 'POST'])
def submit_flavor():
	if request.method == "POST":
		add_user(request.form['name'],request.form['email'], session['flavor_id'])
		return render_template('thanku.html')
	return render_template("submit_flavor.html")

@app.route('/thanku', methods= ['GET', 'POST'])
def thanku():
	return render_template('thanku.html')

@app.route('/vote', methods= ['GET', 'POST'])
def vote():
	if request.method == "POST":
		submit_option(request.form['option'],request.form['user_email'])
		return render_template('thanku.html')
	return render_template('voting.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
	return render_template("thanku.html")

@app.route('/about')
def about():
	return render_template("about_page.html")



# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
