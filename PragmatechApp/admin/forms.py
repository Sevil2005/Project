from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

class AboutPageForm(FlaskForm):
    banner_img = FileField('Əsas Şəkili Redaktə Et', validators=[FileAllowed(['jpg', 'png'])])
    main_text = TextAreaField('Əsas Yazını Redaktə Et')
    second_img = FileField('İkinci Şəkili Redaktə Et', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Redaktə Et')

class QuestionAnswerForm(FlaskForm):
    question = TextAreaField('Sualı Əlavə Et', validators=[DataRequired()])
    answer = TextAreaField('Cavabı Əlavə Et', validators=[DataRequired()])
    submit = SubmitField('Əlavə Et')