from connect_db import session
from models_student import Student

student1 = Student(first_name='Adam', last_name='Bernau')
session.add(student1)
# session.add(Student(first_name="Adam", last_name="Bernau"))       # možný variant

Students = [
    Student(first_name='Adam', last_name='Slobodný'),
    Student(first_name='Alica', last_name='Demečková'),
    Student(first_name='Ciril', last_name='Demočko'),
    Student(first_name='Matúš', last_name='Klaus'),
    Student(first_name='Kamil', last_name='Bauer')
]
session.add_all(Students)

session.commit()

print("Študenti boli pridaný.")