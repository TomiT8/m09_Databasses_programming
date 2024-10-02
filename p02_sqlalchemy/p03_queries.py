from sqlalchemy import and_, or_

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

print("-"*40)
print("Študenti s id >=5:")
"""SELECT * FROM students WHERE student.id >=5"""

rows = session.query(Student).filter(Student.id >= 5)
print(rows)
for row in rows:
    print(row)

print("-"*40)
print("Študenti s id > 3 a priezvyskom začínajúcim na 'Dem':")
# rows = session.query(Student).filter(Student.id > 3, Student.last_name.like("Dem%"))
# rows = session.query(Student).filter(and_(Student.id > 3, Student.last_name.like("Dem%")))
for row in rows:
    print(row)

print("-"*40)
print("Študenti, ktorých meno alebo priezvysko začína na 'A':")
rows = session.query(Student).filter(or_(Student.first_name.like("A%"), Student.last_name.like("A%")))
for row in rows:
    print(row)
