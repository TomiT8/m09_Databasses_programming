from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))

    def __str__(self):
        return f"Student #{self.id} {self.first_name} {self.last_name})"

    def __repr__(self):
        return f"Student(first_name={self.first_name}, last_name={self.last_name})"


class Locker(Base):
    __tablename__ = 'lockers'
    number = Column(Integer, primary_key=True)
    student = Column(Integer, ForeignKey('students.id'))  # Opravená syntax pre cudzie kľúče

    def __repr__(self):
        return f"Locker(number={self.number}, student={self.student})"

    def __str__(self):
        return f"Skrínka #{self.number} patrí študentovi: {self.student}"


class Address(Base):
    __tablename__ = 'address'
    student = Column(Integer, ForeignKey('students.id'), primary_key=True)
    street_name = Column(String(50))
    number = Column(Integer)
    city = Column(String(50))

    def __repr__(self):
        return f"Addres(street_name={self.street_name}, number={self.number}, city={self.city}, student={self.student})"

    def __str__(self):
        return f"Address #{self.street_name}{self.number}, {self.city} patrí študentovi: {self.student}"
