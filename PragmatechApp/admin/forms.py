from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from PragmatechApp.models import session, BannerImg

class BannerImgForm(FlaskForm):
    banner_img = FileField('Əsas Şəkil Redaktə Et', validators=[FileAllowed(['svg', 'jpg', 'png'])])
    page_name = StringField('Səhifənin Adı', validators=[DataRequired()])
    submit = SubmitField('Əlavə Et')

    def validate_page_name(self, page_name):

        name = session.query(BannerImg).filter_by(page_name=page_name.data).first()

        if name:
            raise ValidationError('Daxil etdiyiniz Səhifənin artıq bir əsas şəkili var. Həmin səhifəni tapıb şəkili redaktə edə bilərsiniz.')

class SinglePageBannerImgForm(FlaskForm):
    banner_img = FileField('Əsas Şəkil Redaktə Et', validators=[FileAllowed(['svg', 'jpg', 'png'])])
    submit = SubmitField('Redaktə Et')

class AboutPageForm(FlaskForm):
    banner_img = FileField('Əsas Şəkilin Redaktəsi', validators=[FileAllowed(['svg', 'jpg', 'png'])])
    main_text = TextAreaField('Əsas Yazı')
    second_img = FileField('İkinci Şəkilin Redaktəsi', validators=[FileAllowed(['svg', 'jpg', 'png'])])
    submit = SubmitField('Redaktə Et')

class QuestionAnswerForm(FlaskForm):
    question = TextAreaField('Sualı Əlavə Et', validators=[DataRequired()])
    answer = TextAreaField('Cavabı Əlavə Et', validators=[DataRequired()])
    submit = SubmitField('Əlavə Et')

class CardForm(FlaskForm):
    card_img = FileField('Şəkili Əlavə Et', validators=[FileAllowed(['svg', 'jpg', 'png'])])
    title = TextAreaField('Başlıq', validators=[DataRequired()])
    description = TextAreaField('Təsviri', validators=[DataRequired()])
    submit = SubmitField('Əlavə Et')