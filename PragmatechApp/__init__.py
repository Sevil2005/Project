from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool


app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

engine = create_engine(
    "sqlite:///./site.db", 
    connect_args={"check_same_thread": False}, 
    poolclass=StaticPool
)

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

        
from PragmatechApp.admin.routes import admin
from PragmatechApp.user.routes import user
app.register_blueprint(admin)
app.register_blueprint(user)

