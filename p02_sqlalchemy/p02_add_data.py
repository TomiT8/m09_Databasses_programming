from connect_db import session
from models_student import Student

student1 = Student(first_name='Adam', last_name='Bernau')
session.add(student1)

session.commit()

print("Študent bol pridaný.")