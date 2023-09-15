#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    # Check if all four arguments are provided
    if len(argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(argv[0]))
        exit(1)

    # Extract the arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_to_search = argv[4]

    # Create a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for the State object with the specified name
    state = session.query(State).filter_by(name=state_name_to_search).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()
