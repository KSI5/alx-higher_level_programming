#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa
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

    # Query the State object with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Update the name of the State to "New Mexico"
        state_to_update.name = "New Mexico"
        # Commit the changes to the database
        session.commit()
    else:
        print("State with id=2 not found")

    # Close the session
    session.close()
