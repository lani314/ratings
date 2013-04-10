from flask import Flask, render_template, redirect, request, g, session
import model

app = Flask(__name__)
app.secret_key = 'fishy'

# MAKE 

@app.before_request
def before_request():
	g.id = session.get('id')

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
		session['id'] = id
		return redirect("/movie_search")



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


@app.route("/movie_search", methods=["GET"])
def user_search():

	
	# query for movie information by id
	# movie = model.session.query(model.Movie).get(id)

	# render template
	return render_template("movie_search.html")

@app.route("/movie_search", methods=["POST"])
def display_search():

	# retrieving user input from search form
	query = request.form['search']
	# query from movie class and filter name of movies via the ilike function
	# ilike = search matched data
	# if there is match, print all matching data up to 30
	movies = model.session.query(model.Movie).\
		filter(model.Movie.name.ilike("%" + query + "%")).\
		limit(30).all()


	# render template and pass query into template
	# pass on movies query to go be iterated through in results html page
	return render_template("results.html", movies=movies)

@app.route("/add_rating")
def new_user():
	# return template of login form
	return render_template("add_rating.html")

@app.route("/save_addedrating", methods=["POST"])
def add_user():

	add_rating = request.form['added_rating']

	saved_ratingadd = Rating(movie_id=row[1], user_id=row[0], rating=row[2])
            session.add(saved_ratingadd)

	return redirect("/")
 

@app.route("/users_all/<int:id>", methods=["GET"])
def users_all(id):
	# id = session.get("id")
	# query for info on user id, defined as user variable
	user = model.session.query(model.User).get(id)

	# get user and ratings joining, defined as variable 
	ratings = user.ratings
	#print ratings

	# loop through the ratings
	# for rating in ratings:
	# 	# rating and movie join, defined as variable
	# 	print rating.rating
	# 	print rating.movie.name
	# 	#movie = rating.movie
		# we should now have our movies and ratings for the user??

	# return template with user ratings and movie titles
	return render_template("users_all.html", ratings=ratings)

	# print movie.name, rating.rating
	
	# return "URL works %d"%id
 

if __name__ == "__main__":
	app.run(debug = True)


