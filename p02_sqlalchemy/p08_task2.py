from datetime import datetime
from connect_db import session, db
from models_student import *
from sqlalchemy.exc import IntegrityError

# Base.metadata.create_all(db)
#
# try:
#     session.add_all(
#         [
#             Grades(student=1, grade='A', data_create=datetime(2024,10,1)),
#             Grades(student=3, grade='B', data_create=datetime(2024,10,3)),
#             Grades(student=4, grade='D', data_create=datetime(2024,10,2)),
#             Grades(student=5, grade='E', data_create=datetime(2024,10,3)),
#             Grades(student=6, grade='FX', data_create=datetime(2024,10,8)),
#             Grades(student=7, grade='A', data_create=datetime(2024, 10, 3)),
#             Grades(student=1, grade='B', data_create=datetime(2024, 10, 13)),
#             Grades(student=1, grade='A', data_create=datetime(2024, 10, 1)),
#             Grades(student=3, grade='FX', data_create=datetime(2024, 10, 8)),
#             Grades(student=4, grade='D', data_create=datetime(2024, 10, 13)),
#             Grades(student=5, grade='E', data_create=datetime(2024, 10, 3)),
#             Grades(student=6, grade='E', data_create=datetime(2024, 10, 18)),
#             Grades(student=7, grade='A', data_create=datetime(2024, 10, 3)),
#             Grades(student=1, grade='B', data_create=datetime(2024, 10, 30))
#         ]
#     )
#
#     session.commit()
#
# except IntegrityError as e:
#     session.rollback()
#     print(f"ERROR: {e}")

print("Všetky známky - výpis vo formáte: meno a priezvisko študenta: známka")
print("Všetky známky pre každého študenta:")
print("Zmazanie najnovšej známky")
print("Výpis priemernej známky pre každého študenta:")
print("Študent s najlepším priemerným hodnotením")
print("Zmazanie najstaršej známky")