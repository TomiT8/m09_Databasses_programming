from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from connection_details import *

# db = create_engine('mysql+mysqlconnector://test:test@localhost:3306/cinematic')

CONNECTION_SREING = "mysql+mysqlconnector://{user}:{password}@{host}:3306/{database}"
db = create_engine(CONNECTION_SREING.format(user=user, password=password, host=host, database='school'))


Session = sessionmaker(bind=db)
session = Session()

# print (f"db.url = {db.url}")