from connect_db import session, db
from models_student import *
from sqlalchemy.exc import IntegrityError

# Base.metadata.create_all(db)

# try:
#     session.add_all(
#         [
#             Address(street_name="Komenského", number=10, city="Košice", student=1),
#             Address(street_name="Rastislavova", number=15, city="Košice", student=6),
#             Address(street_name="Obrancov Mieru", number=2, city="Košice", student=3),
#             Address(street_name="Stará Spišská cesta", number=33, city="Košice", student=4),
#             Address(street_name="Kováčska", number=1, city="Košice", student=5),
#         ]
#     )
#
#     # session.commit()
#
# except IntegrityError as e:
#     session.rollback()
#     print(f"ERROR: {e}")


print("Všetci študenti a ich adresy:")
rows = session.query(Student, Address).join(Address)
for student, address in rows:
    print(f"{student}: {address}")

print('-'*80)
print("Môžeme zmeniť poradie tabuliek vo výstupe")
rows1 = session.query(Address, Student).join(Address)
for address, student in rows1:
    print(f"{student}: {address}")

print('-'*80)
print("Všetci študenti z Košíc:")
#rows = session.query(Student, Address).join(Address).filter(Address.city == "Košice")
rows_Brno = rows.filter(Address.city == "Košice")  # nebo lze využít předchozí výsledek
for student, address in rows_Brno:
    print(f"{student}: {address}")

print('-'*80)
print("Všetci študenti z Košíc usporiadaný  abecedne podľa priezviska:")
#rows = session.query(Student, Address).join(Address).filter(Address.city == "Brno").order_by(Student.last_name)
rows_Brno_sorted = rows_Brno.order_by(Student.last_name)  # lze opět využít předchozí výsledek
for student, address in rows_Brno_sorted:
    print(f"{student}: {address}")

print('-'*80)
print("Zmeniť adresu Adama Bernaua na ulicu 'Vedľajšia':")
students = session.query(Student, Address).join(Address).filter(Student.first_name == "Adam", Student.last_name == "Bernau")
for student, address in students:
    print(f"{student}: {address}")
print('-'*40)
student, address = students[0]
print(f"{student}: {address}")
address.street_name = "Vedľejšia"
session.commit()
print('-'*40)
student, address = students[0]
print(f"{student}: {address}")
