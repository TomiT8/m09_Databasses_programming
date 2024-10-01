from connect_db import session
from models_student import Student

print("")
print("Všetci študenti v databáze:")

students = session.query(Student).all()

for student in students:
    print(student)

print("-"*50)
total = session.query(Student).count()
print(f"Počet študentov v databáze: {total}")
