#!/usr/bin/env python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Define connection parameters
    mysql_username, mysql_password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create SQLAlchemy engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and their associated City objects
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    # Close the session
    session.close()
