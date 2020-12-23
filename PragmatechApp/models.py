from PragmatechApp import db

class AboutPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    banner_img = db.Column(db.String(20), nullable=False)
    main_text = db.Column(db.String(100), nullable=False)
    second_img = db.Column(db.String(20), nullable=False)

class QuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)