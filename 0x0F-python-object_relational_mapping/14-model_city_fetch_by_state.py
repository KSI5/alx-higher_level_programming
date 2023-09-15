#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    # Check if all three arguments are provided
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(argv[0]))
        exit(1)

    # Extract the arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Create a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects and order them by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
