from connect_db import session
from models_student import Student, Locker

print("Spojíme študentov so skrinkami, študenti, ktorý majú skrinku")
rows = session.query(Student).join(Locker)
for row in rows:
    print(row)

print("-"*40)
rows = session.query(Student, Locker).join(Locker)
for row in rows:
    print(row)
print("-"*40)
for row in rows:
    student, locker = row
    print(f"{locker}: {student}")

print("-"*40)
print("Študent so skrinkou #4")
rows = session.query(Student).join(Locker).filter(Locker.number == 4)
for row in rows:
    print(row)

print("-"*40)
print("Usporiadanie podľa čísla skrinky")
rows = session.query(Student, Locker).join(Locker).order_by(Locker.number)
print(rows)
for row in rows:
    print(row)
    print(f"Skrinka #{row[1].number} patrí študentovi {row[0]}")
print("-"*40)
for student, locker in rows:
    print(f"{locker}: {student}")
