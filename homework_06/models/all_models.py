from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .database import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    confirmed = Column(Boolean, nullable=False, default=False)
    confirmed_at = Column(DateTime, nullable=True)
    places = relationship('Place', backref='user')
    is_admin = Column(Boolean, nullable=True, default=False)

    def __repr__(self):
        return f'User {self.username}'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Category(db.Model):
    id = Column(Integer, primary_key=True)
    name_category = Column(String(30), unique=True, nullable=False)
    places = relationship('Place', backref='category')

    def __repr__(self):
        return f'{self.name_category}'


class City(db.Model):
    id = Column(Integer, primary_key=True)
    name_city = Column(String(70), unique=True, nullable=False)
    places = relationship('Place', backref='city')

    def __repr__(self):
        return f'{self.name_city}'


class Place(db.Model):
    id = Column(Integer, primary_key=True)
    name_place = Column(String(70), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    rate = Column(Float(), nullable=False)

    def __repr__(self):
        return f'{self.name_place}'
