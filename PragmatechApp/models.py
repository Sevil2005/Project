import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///./site.db")

Base = declarative_base(engine)

class AboutPage(Base):
    __tablename__ = 'AboutPage'
    id = db.Column(db.Integer, primary_key=True)
    banner_img = db.Column(db.String(20), nullable=False)
    main_text = db.Column(db.String(100), nullable=False)
    second_img = db.Column(db.String(20), nullable=False)
    third_img = db.Column(db.String(20), nullable=False)

class QuestionAnswer(Base):
    __tablename__ = 'QuestionAnswer'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

Session = sessionmaker(engine)
session = Session()