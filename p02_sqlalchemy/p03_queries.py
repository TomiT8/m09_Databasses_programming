from sqlalchemy import and_, or_, desc

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

print("-"*40)
print("Všetci študenti usporiadaný podľa priezviska:")
rows = session.query(Student).order_by(Student.last_name, Student.first_name)
for row in rows:
    print(row)

print("-"*40)
print("Všetci študenti usporiadaný podľa priezviska zostupne:")
rows = session.query(Student).order_by(desc(Student.last_name), desc(Student.first_name))
for row in rows:
    print(row)

print("-"*40)
print("Študenti s id >= 5 usporiadaný abecedne podľa priezviska:")
rows = session.query(Student).filter(Student.id >= 5).order_by(Student.last_name)
for row in rows:
    print(row)

print("-"*40)
print("Offset = 3 (preskočí prvé 3 záznami):")
rows = session.query(Student).offset(3)
for row in rows:
    print(row)

print("-"*40)
print("Prvý študent:")
rows = session.query(Student).limit(1)
for row in rows:
    print(row)
print("-"*40)
print(rows[0])
print("-"*40)
result = session.query(Student).first()
print(result)


print("-"*40)
print("Student s id == 3")
rows = session.query(Student).filter(Student.id == 3)
for row in rows:
    print(row)
print("-"*40)
result = session.query(Student).get(3)
print(result)
