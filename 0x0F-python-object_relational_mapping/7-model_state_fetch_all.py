#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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

    # Query all State objects and order them by states.id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
