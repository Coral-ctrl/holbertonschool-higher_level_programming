#!/usr/bin/python3
"""script that prints all City objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Create engine: establishes connection to MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(
        State.id == City.state_id
    )order_by(City.id).all()

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session to release the connection
    session.close()
