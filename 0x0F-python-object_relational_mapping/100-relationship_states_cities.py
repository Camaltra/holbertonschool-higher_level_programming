#!/usr/bin/python3

"""
Create a cities, related to a state
"""

import sys
from relationship_state import State
from relationship_city import Base, City

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
    session.add(City(name="San Fransisco", state=State(name="California")))
    session.commit()
    session.close()