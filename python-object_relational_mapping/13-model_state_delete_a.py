#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter a from the database.
"""
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
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()

    # Close session to release the connection
    session.close()
