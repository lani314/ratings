from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():
	user_list = model.session.query(model.User).limit(25).all()

	print user_list
	return render_template("user_list.html", users=user_list)

# create login route
@app.route("/login")
def login():
	# return template of login form
	return render_template("login.html")

# create authenticate route for after user input info
# use methods POST in order to 
@app.route("/authenticate", methods=["POST"])
def authenticate():
	# make variable for email input of user in form
	# request.form is built-in function to retrieve form info
	email = request.form['email']
	# make variable for password input of user in form
	password = request.form['password']

	# create query for to filter info from user table (authentication process)
	user = model.session.query(model.User).filter_by(email=email,
		password=password).first()

	# if not in table
	if not user:
		# redirect user to login page
		return redirect("/login")
	else:
		# if info in table, redirect user to index page
		return redirect("/")

@app.route("/new_user")
def new_user():
	# return template of login form
	return render_template("new_user.html")

@app.route("/save_user", methods=["POST"])
def add_user():
	# make variable for email input of user in form
	# request.form is built-in function to retrieve form info
	email = request.form['email']
	# make variable for password input of user in form
	password = request.form['password']	

	add_user = model.User()

	add_user.email = email

	add_user.password = password

	model.session.add(add_user)
	model.session.commit()

	return redirect("/")	


#@app.route("/", methods=["POST"])
def user_get_info():

	# someone clicks on user 

	# from user id initiate query

	user_get = model.session.query(model.User).get(i).filter_by("ratings").all()

	#  from ratings_id query the movie names

	return redirect(" ")	

	
if __name__ == "__main__":
	app.run(debug = True)














