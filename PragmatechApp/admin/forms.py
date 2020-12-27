from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError

class BannerImgForm(FlaskForm):
    banner_img = FileField('Əsas Şəkil Redaktə Et', validators=[FileAllowed(['svg', 'jpg', 'png', 'html'])])
    page_name = StringField('Səhifənin Adı', validators=[DataRequired()])
    submit = SubmitField('Əlavə Et')

class AboutPageForm(FlaskForm):
    banner_img = FileField('Əsas Şəkilin Redaktəsi', validators=[FileAllowed(['svg', 'jpg', 'png', 'html'])])
    main_text = TextAreaField('Əsas Yazı')
    second_img = FileField('İkinci Şəkilin Redaktəsi', validators=[FileAllowed(['svg', 'jpg', 'png', 'html'])])
    submit = SubmitField('Redaktə Et')

class QuestionAnswerForm(FlaskForm):
    question = TextAreaField('Sualı Əlavə Et', validators=[DataRequired()])
    answer = TextAreaField('Cavabı Əlavə Et', validators=[DataRequired()])
    submit = SubmitField('Əlavə Et')

class CardForm(FlaskForm):
    card_img = FileField('Şəkili Əlavə Et', validators=[FileAllowed(['svg', 'jpg', 'png', 'html'])])
    title = TextAreaField('Başlıq', validators=[DataRequired()])
    description = TextAreaField('Təsviri', validators=[DataRequired()])
    submit = SubmitField('Əlavə Et')