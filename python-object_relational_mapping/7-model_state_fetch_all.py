#!/usr/bin/python3
"""script that lists all State objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create engine: establishes connection to MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Base.metadata.bind = engine

    # Create session factory bound to the engine, then open a session
    # Session is the "conversation" with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects, sorted by id ascending
    # SQLAlchemy translates this to: SELECT * FROM states ORDER BY id ASC
    states = session.query(State).order_by(State.id).all()

    # Print each state as "id: name" using object attributes
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session to release the connection
    session.close()
