import csv
import model
# from model import User, Movie, Rating 
from model import Movie, User, Rating
from sys import argv
from datetime import datetime

script, filename, filename1, filename2 = argv
#script, u.user, u.data, u.item

def load_users(session):
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter ='|')
        print reader
        for row in reader:

            add_object = User(id=row[0], age=row[1], zip_code=row[4])
            session.add(add_object)
        session.commit()


def load_movies(session):
    with open(filename1, 'rb') as csvfile:
        reader1 = csv.reader(csvfile, delimiter ='|')
        
        for row in reader1:
            if row[2] == "":
                released_at = datetime.strptime('01-Jan-1900', '%d-%b-%Y')
            else:
                released_at = datetime.strptime(row[2], '%d-%b-%Y')     
            #print released_at
        
            if row[1] == "":
                pass
            else:
                title = row[1]
                title = title.decode("latin -1")
            #print title
       
                add_object3 = Movie(id = row[0], name = title, released_at = released_at, imdb_url = row[4])
                session.add(add_object3)
            session.commit()


def load_ratings(session):
    #user = 0
    #item = 1
    #rating = 2
    #timestamp = 3
    with open(filename2, 'rb') as csvfile:
        reader2 = csv.reader(csvfile, delimiter ='\t')
        for row in reader2:
            add_object2 = Rating(movie_id=row[1], user_id=row[0], rating=row[2])
            session.add(add_object2)
        session.commit()


 

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    
    
    load_movies(session)
    

    load_ratings(session)
    

if __name__ == "__main__":
    s = model.connect()
    main(s)
