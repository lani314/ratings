from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import datetime

ENGINE = None
Session = None


Base = declarative_base()

### Class declarations go here

class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key = True)
	email = Column(String(64), nullable=True)
	password = Column(String(64), nullable=True)
	age = Column(Integer, nullable=True)
	zip_code = Column(String(15), nullable=True)


# id: integer
# age: integer
# gender: string
# zip_code: string (technically zip codes aren't numeric)
# email: optional string
# password: optional string



class Movie(Base):
	__tablename__ = "movies"

	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable=True)
	released_at = Column(DateTime, default=datetime.datetime.utcnow)
	imdb_url = Column(String(300), nullable=True)

class Rating(Base):
	__tablename__ = "ratings"
	id = Column(Integer, primary_key = True)
	movie_id = Column(Integer, nullable = True)
	user_id = Column(Integer, nullable = True)
	rating = Column(Integer, nullable = True)


### End class declarations

def connect():
	global ENGINE
	global Session

	ENGINE = create_engine("sqlite:///ratings.db", echo=True)
	Session = sessionmaker(bind=ENGINE)

	return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()

