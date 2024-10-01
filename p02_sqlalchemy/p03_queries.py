from connect_db import session
from models_student import Student

print("-"*40)
print("Všetci študenti v databáze:")

students = session.query(Student).all()

for student in students:
    print(student)

print("-"*40)
total = session.query(Student).count()
print(f"Počet študentov v databáze: {total}")
