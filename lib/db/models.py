from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lawyer(Base):
    __tablename__ = 'lawyers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    cases = relationship('Case', back_populates='lawyer')
    clients = relationship('Client', back_populates='lawyer')

class Case(Base):
    __tablename__ = 'cases'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    lawyer_id = Column(Integer, ForeignKey('lawyers.id'), nullable=False)

    lawyer = relationship('Lawyer', back_populates='cases')

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    lawyer_id = Column(Integer, ForeignKey('lawyers.id'), nullable=False)

    lawyer = relationship('Lawyer', back_populates='clients')
