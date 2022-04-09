#!/usr/bin/python3

"""
List all state corresponding to cities

Adding commenting
"""

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")
        for city in (
            session.query(City).filter(state.id == City.state_id).
            order_by(City.id)
        ):
            print("    {}: {}".format(city.id, city.name))
    session.close()
