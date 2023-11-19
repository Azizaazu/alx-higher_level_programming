#!/usr/bin/python3
""" script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)
    session.commit()
    session.close()
