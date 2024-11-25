import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__= 'planet'
#primary_key es para  identificar algo que es único y especifico
    id = Column(Integer,primary_key=True)
    name=Column(String(200))
    population= Column(Integer)
    weather=Column(String(50), nullable=False)

class Character(Base):
    __tablename__="character"
    
    id=Column(Integer,primary_key=True)
    name=Column(String(200))
    zodiac=Column(String(100))




class Favorite(Base):
    __tablename__='favorite'

    id=Column(Integer, primary_key=True)
    character_id=Column(Integer,ForeignKey('character.id'))
    character = relationship(Character)

    user_id=Column(Integer,ForeignKey('user.id'))
    user = relationship(User)

    planet_id=Column(Integer,ForeignKey('planet.id'))
    planet = relationship(Planet)
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
