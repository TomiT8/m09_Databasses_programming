# pip install sqlalchemy
from sqlalchemy_utils import database_exists, create_database
from connect_db import *
from models_student import Base

print(f"db.url = {db.url}")

if not database_exists(db.url):         # vytvorí novú schému
    create_database(db.url)

Base.metadata.create_all(db)            # vytvorí tabuľky z tried definovaných v models_students.py
