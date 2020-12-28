import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///./site.db",
connect_args={'check_same_thread': False})

Base = declarative_base(engine)

class BannerImg(Base):
    __tablename__ = 'BannerImg'
    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(50), nullable=False)
    banner_img = db.Column(db.String(100), nullable=False)

class AboutPage(Base):
    __tablename__ = 'AboutPage'
    id = db.Column(db.Integer, primary_key=True)
    banner_img = db.Column(db.String(20), nullable=False)
    main_text = db.Column(db.String(100), nullable=True)
    second_img = db.Column(db.String(20), nullable=True)

class QuestionAnswer(Base):
    __tablename__ = 'QuestionAnswer'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

class Advantage(Base):
    __tablename__ = 'Advantage'
    id = db.Column(db.Integer, primary_key=True)
    svg_img = db.Column(db.String(100), nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

class Package(Base):
    __tablename__ = 'Package'
    id = db.Column(db.Integer, primary_key=True)
    pack_img = db.Column(db.String(100), nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

class AdmissionStage(Base):
    __tablename__ = 'AdmissionStage'
    id = db.Column(db.Integer, primary_key=True)
    stage_img = db.Column(db.String(100), nullable=False)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

Session = sessionmaker(engine)
session = Session()