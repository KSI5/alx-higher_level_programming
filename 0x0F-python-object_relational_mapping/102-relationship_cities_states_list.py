#!/usr/bin/env python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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

    # Query all City objects with their associated State objects
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
