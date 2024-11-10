# TODO: Use data in medical-data.json to create a new collection: medicaldata
# TODO: I Find all rows with procedure_code equal 0F1F4ZC
# TODO: I Find patient with patient_id equal 74 , print his full name
# TODO: I Find a procedure performed on 2019-05-24T01:52:37.000Z and
# TODO: update its procedure code to 0F1F4ZC

"""
Bez SQL
"""

# import json
# from dataclasses import dataclass
# from typing import List
#
#
# @dataclass
# class Medical:
#     patient_id: int
#     first_name: str
#     last_name: str
#     gender: str
#     procedure_code: str
#     procedure_description: str
#     diagnosis: str
#     visit_date: dict
#
#     def __repr__(self):
#         return (f'{self.patient_id} - {self.first_name} {self.last_name} - {self.gender} - '
#                 f'{self.procedure_code} - {self.procedure_description} - {self.diagnosis} - '
#                 f'{self.visit_date}')
#
#     def get_full_name(self) -> str:
#         return f"{self.first_name} {self.last_name}"
#
#     def get_procedure_code(self) -> str:
#         return f"{self.procedure_code}"
#
# def load_medical_data(file_name) -> List[Medical]:
#     medical_data = []
#     with open(file_name) as file:
#         data = json.load(file)
#         for record in data:
#             medical_data.append(Medical(**record))
#     return medical_data
#
#
# def find_procedure_code(medicaldatas: List[Medical], procedure_code: str) -> List[Medical]:
#     found_records = []
#     for record in medicaldatas:
#         if record.procedure_code == procedure_code:
#             found_records.append(record)
#             print(f'Found record: {record}')
#             print("")
#     return found_records
#
#
# def find_patient_by_id(medicaldatas: List[Medical], patient_id: int):
#     for record in medicaldatas:
#         if record.patient_id == patient_id:
#             return record
#     return None
#
#
# def find_procedure_by_visit_date(medicaldatas: List[Medical], visit_date: str):
#     for record in medicaldatas:
#         if record.visit_date["date"] == visit_date:
#             return record
#     return None
#
# def save_medical_data(file_name, medicaldatas):
#     with open(file_name, 'w') as file:
#         json.dump([record.__dict__ for record in medicaldatas], file, indent=4)
#     print('Data successfully written to file.')
#
#
# if __name__ == "__main__":
#     file_name = r'files\medical-data.json'
#     medicaldatas = load_medical_data(file_name)
#
#     print("*" * 80)
#     procedure_code_find = '0F1F4ZC'
#     print(f"All rows with procedure_code equal {procedure_code_find}:")
#     found_record = find_procedure_code(medicaldatas, procedure_code_find)
#
#     print("*" * 80)
#     patient_id_find = 74
#     print(f"Patient with patient_id equal  {patient_id_find}::")
#     patient_name = find_patient_by_id(medicaldatas, patient_id_find)
#     if patient_name:
#         print(f'{patient_name.get_full_name()}')
#     else:
#         print('No record found with the specified patient ID.')
#     print("")
#
#     print("*" * 80)
#     visit_date_find = "2019-05-24T01:52:37.000Z"
#     print(f"Procedure performed on {visit_date_find}:")
#     procedure_record = find_procedure_by_visit_date(medicaldatas, visit_date_find)
#     if procedure_record:
#         print(f'Current procedure code: {procedure_record.get_procedure_code()}')
#
#         procedure_record.procedure_code = '0F1F4ZC'
#         print(f'Procedure code updated to {procedure_record.procedure_code}.')
#         save_medical_data(file_name, medicaldatas)
#     else:
#         print('No procedure found on the specified date.')
#
#     print("*" * 80)

"""
Pomocou SQL slchemy
"""

# import json
# from sqlalchemy import create_engine, Column, Integer, String, JSON
# from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy_utils import database_exists, create_database
# from typing import List
#
# host = "localhost"
# user = "test"
# password = "test"
#
# CONNECTION_STRING = "mysql+mysqlconnector://{user}:{password}@{host}:3306/{database}"
# db = create_engine(CONNECTION_STRING.format(user=user, password=password, host=host, database='medical_data'))
#
# if not database_exists(db.url):
#     create_database(db.url)
#
# Session = sessionmaker(bind=db)
# session = Session()
#
# Base = declarative_base()
#
#
# class Medical(Base):
#     __tablename__ = 'medical_records'
#
#     id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#     patient_id = Column(Integer, nullable=False)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     gender = Column(String(10), nullable=False)
#     procedure_code = Column(String(50), nullable=False)
#     procedure_description = Column(String(255), nullable=False)
#     diagnosis = Column(String(255), nullable=False)
#     visit_date = Column(JSON, nullable=False)
#
#     def __repr__(self):
#         return (f'{self.patient_id} - {self.first_name} {self.last_name} - {self.gender} - '
#                 f'{self.procedure_code} - {self.procedure_description} - {self.diagnosis} - '
#                 f'{self.visit_date}')
#
#     def get_full_name(self) -> str:
#         return f"{self.first_name} {self.last_name}"
#
#     def get_procedure_code(self) -> str:
#         return f"{self.procedure_code}"
#
#
# Base.metadata.create_all(db)
#
# file_name = r'files\medical-data.json'
# with open(file_name, 'r') as file:
#     data = json.load(file)
#     for entry in data:
#         record = Medical(
#             patient_id=entry["patient_id"],
#             first_name=entry["first_name"],
#             last_name=entry["last_name"],
#             gender=entry["gender"],
#             procedure_code=entry["procedure_code"],
#             procedure_description=entry["procedure_description"],
#             diagnosis=entry["diagnosis"],
#             visit_date=entry["visit_date"]
#         )
#         session.add(record)
#
# session.commit()
# print("Dáta boli úspešne vložené do databázy.")
#
#
# def find_procedure_code(medicaldatas: List[Medical], procedure_code: str) -> List[Medical]:
#     found_records = []
#     for record in medicaldatas:
#         if record.procedure_code == procedure_code:
#             found_records.append(record)
#             print(f'Found record: {record}')
#             print("")
#     return found_records
#
#
# def find_patient_by_id(medicaldatas: List[Medical], patient_id: int):
#     for record in medicaldatas:
#         if record.patient_id == patient_id:
#             return record
#     return None
#
#
# def find_procedure_by_visit_date(medicaldatas: List[Medical], visit_date: str):
#     for record in medicaldatas:
#         if record.visit_date["date"] == visit_date:
#             return record
#     return None
#
#
# def update_procedure_code(medicaldatas: List[Medical], old_procedure_code: str, new_procedure_code: str):
#     for record in medicaldatas:
#         if record.procedure_code == old_procedure_code:
#             print(f'Updating record: {record}')
#             record.procedure_code = new_procedure_code
#             session.commit()
#             print(f'Updated procedure code to {new_procedure_code}')
#             return record
#     print(f'No record found with procedure code {old_procedure_code}')
#     return None
#
#
# if __name__ == "__main__":
#
#     medicaldatas = session.query(Medical).all()
#
#     print("")
#     print("*" * 80)
#     procedure_code_find = '0F1F4ZC'
#     print(f"All rows with procedure_code equal {procedure_code_find}:")
#     found_record = find_procedure_code(medicaldatas, procedure_code_find)
#
#     print("*" * 80)
#     patient_id_find = 74
#     print(f"Patient with patient_id equal  {patient_id_find}::")
#     patient_name = find_patient_by_id(medicaldatas, patient_id_find)
#     if patient_name:
#         print(f'{patient_name.get_full_name()}')
#     else:
#         print('No record found with the specified patient ID.')
#     print("")
#
#     print("*" * 80)
#     visit_date_find = "2019-05-24T01:52:37.000Z"
#     print(f"Procedure performed on {visit_date_find}:")
#     procedure_record = find_procedure_by_visit_date(medicaldatas, visit_date_find)
#     if procedure_record:
#         print(f'Current procedure code: {procedure_record.get_procedure_code()}')
#
#         procedure_record.procedure_code = '0F1F4ZC'
#         print(f'Procedure code updated to {procedure_record.procedure_code}.')
#         session.commit()
#     else:
#         print('No procedure found on the specified date.')
#
#     print("*" * 80)
#     old_procedure_code = '041L0AJ'
#     new_procedure_code = '0F1F4ZC'
#     print(f"Updating procedure code from {old_procedure_code} to {new_procedure_code}:")
#     updated_record = update_procedure_code(medicaldatas, old_procedure_code, new_procedure_code)
#
#     if updated_record:
#         print(f'Updated record: {updated_record}')
#     else:
#         print('No record found to update.')