#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker  # Import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.bind = engine

    # Create the tables
    Base.metadata.create_all()

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Add some sample records
    student1 = Student(name='John Doe')
    student2 = Student(name='Jane Smith')

    session.add_all([student1, student2])
    session.commit()

    # Query all students and print their names
    students = session.query(Student).all()
    for student in students:
        print(f"Student ID: {student.id}, Name: {student.name}")
