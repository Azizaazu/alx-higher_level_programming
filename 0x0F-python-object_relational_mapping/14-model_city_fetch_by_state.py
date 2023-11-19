#!/usr/bin/python3
"""Script that prints all City objects from the hbtn_0e_14_usa database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State.name).filter_by(id=city.state_id).first()[0]
        print("{}: ({}) {}".format(state_name, city.id, city.name))

        session.close()
