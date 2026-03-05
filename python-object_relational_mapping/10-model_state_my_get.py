#!/usr/bin/python3
"""
Script that prints the State object with the name passed as
argument from the database.
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

    state = session.query(State).filter_by(
        State.name=sys.argv[4]
    ).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close session to release the connection
    session.close()
