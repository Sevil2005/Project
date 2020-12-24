import os
from flask import Flask, render_template, url_for, redirect, request, Blueprint
from PragmatechApp import app
from PragmatechApp.models import session, AboutPage, QuestionAnswer
from PragmatechApp.admin.forms import AboutPageForm, QuestionAnswerForm
from werkzeug.utils import secure_filename

admin = Blueprint('admin', __name__, template_folder="templates")

@admin.route('/dashboard')
def index():
    return render_template('admin_layout.html')

# About Banner Section

@admin.route('/dashboard/səhifələr/haqqımızda')
def about():
    datas = session.query(AboutPage).all()
    questions = session.query(QuestionAnswer).all()
    return render_template('pages/admin_about.html', datas=datas, questions=questions)

@admin.route('/dashboard/səhifələr/haqqımızda/Banner-Section/redaktə-et/<int:id>', methods = ['GET', 'POST'])
def about_edit(id):
    form = AboutPageForm()
    selectedData = session.query(AboutPage).get(id)
    if form.validate_on_submit():
        if form.banner_img.data:
            uploaded_banner_file = request.files['banner_img']
            banner_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], banner_filename))
            selectedData.banner_img = banner_filename
        if form.second_img.data:
            uploaded_second_file = request.files['second_img']
            second_filename = secure_filename(uploaded_second_file.filename)
            uploaded_second_file.save(os.path.join(app.config['UPLOAD_PATH'], second_filename))
            selectedData.second_img = second_filename
        
        selectedData.main_text = form.main_text.data
        session.commit()
        return redirect(url_for('admin.about'))
    elif request.method =='GET':
        form.main_text.data = selectedData.main_text
    return render_template('pages/admin_about_edit.html', form=form)

# About Question-Answer Section

@admin.route('/dashboard/səhifələr/haqqımızda/Sual-Cavab/əlavə-et', methods = ['GET', 'POST'])
def about_que_add():
    form = QuestionAnswerForm()
    if form.validate_on_submit():
        new_que = QuestionAnswer(question = form.question.data, answer = form.answer.data)
        session.add(new_que)
        session.commit()
        return redirect(url_for('admin.about'))
    return render_template('pages/admin_about_que.html', form=form)

@admin.route('/dashboard/səhifələr/haqqımızda/Sual-Cavab/redaktə-et/<int:id>', methods = ['GET', 'POST'])
def about_que_edit(id):
    selectedData = session.query(QuestionAnswer).get(id)
    form = QuestionAnswerForm()
    if form.validate_on_submit():
        selectedData.question = form.question.data
        selectedData.answer = form.answer.data
        session.commit()
        return redirect(url_for('admin.about'))
    elif request.method =='GET':
        form.question.data = selectedData.question
        form.answer.data = selectedData.answer
    return render_template('pages/admin_about_que.html', form=form)

@admin.route('/dashboard/səhifələr/haqqımızda/Sual-Cavab/sil/<int:id>', methods = ['GET'])
def about_que_delete(id):
    selectedData = session.query(QuestionAnswer).get(id)
    session.delete(selectedData)
    session.commit()
    return redirect(url_for('admin.about'))

