import model
import csv
import datetime
from model import Movie
from sys import argv
script, filename1 = argv



# def load_users(session):
#     with open(filename, 'rb') as csvfile:
#         reader = csv.reader(csvfile, delimiter ='|')
#         print reader
#         for row in reader:

             add_object = User(id=row[0], age=row[1], zip_code=row[4])
#             session.add(add_object)
#         session.commit()

# f = open(filename)
# read = f.read(50)
# print read
    # # use u.user
    # with open(filename, 'rb') as f:
    #     reader = csv.reader(f)
    #     # for row in reader1:
    #     #     print row
    #     session.add_all([
    #         User('')

def load_movies(session):
    with open(filename1, 'rb') as csvfile:
        reader1 = csv.reader(csvfile, delimiter ='|')
       # b = datetime.strptime(release_date, '%d-%b-%Y')
        for row in reader1:
            add_object3 = Movie(id = row[0], name = row[1], released_at = row[2], imdb_url=row[3])
            

#     with open(filename2, 'rb') as f:
#         reader2 = csv.reader(f)
        # for row in reader2:
        #     print row

# def load_ratings(session):
#     with open(filename2, 'rb') as csvfile:
#         reader2 = csv.reader(csvfile, delimiter ='\t')
#         print reader2
#         for row in reader2:
            
#             add_object2 = Rating(id=row[0], user_id=row[1], movie_id=row[2], rating=row[3])
#             session.add(add_object2)
#             session.commit()
#     with open(filename3, 'rb') as f:
#         reader3 = csv.reader(f)
        # for row in reader3:
        #     print row

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    # load_users(session)
    
    
    # load_movies(session)
    

    load_ratings(session)
    

if __name__ == "__main__":
    s= model.connect()
    main(s)
