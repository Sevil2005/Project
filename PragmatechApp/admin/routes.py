import os
from flask import Flask, render_template, url_for, redirect, request, Blueprint
from PragmatechApp import app, user
from PragmatechApp.models import session, AboutPage, QuestionAnswer, Advantage, BannerImg, Package, AdmissionStage
from PragmatechApp.admin.forms import BannerImgForm, AboutPageForm, QuestionAnswerForm, CardForm, SinglePageBannerImgForm
from werkzeug.utils import secure_filename

admin = Blueprint('admin', __name__, template_folder="templates")

@admin.route('/dashboard')
def index():
    return render_template('admin_layout.html')

# <--------------------------------------- Add Page Banner --------------------------------------------------------->

@admin.route('/dashboard/səhifələr/banner-əlavə-et', methods = ['GET', 'POST'])
def banner_add():
    form = BannerImgForm()
    banner_imgs = session.query(BannerImg).all()
    if form.validate_on_submit():
        uploaded_file = request.files['banner_img']
        banner_file = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], banner_file))

        if form.page_name.data == "Haqqımızda":
            about_banner = AboutPage(banner_img = banner_file)
            session.add(about_banner)

        new_banner = BannerImg(banner_img = banner_file, page_name = form.page_name.data)
        session.add(new_banner)
        session.commit()
        return redirect(url_for('admin.banner_add'))
    return render_template('admin_banner_add.html', form=form, banner_imgs=banner_imgs)

@admin.route('/dashboard/səhifələr/banner-sil/<int:id>', methods = ['GET'])
def banner_delete(id):
    selectedData = session.query(BannerImg).get(id)
    session.delete(selectedData)
    session.commit()
    return redirect(url_for('admin.banner_add'))

# <--------------------------------------- Admin About Page --------------------------------------------------------->

# About Banner Section

@admin.route('/dashboard/səhifələr/haqqımızda')
def about():
    datas = session.query(AboutPage).all()
    questions = session.query(QuestionAnswer).all()
    return render_template('admin_about_page/admin_about.html', datas=datas, questions=questions)

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
        return redirect(url_for('user.about'))
    elif request.method =='GET':
        form.main_text.data = selectedData.main_text
    return render_template('admin_about_page/admin_about_edit.html', form=form)

# About Question-Answer Section

@admin.route('/dashboard/səhifələr/haqqımızda/Sual-Cavab/əlavə-et', methods = ['GET', 'POST'])
def about_que_add():
    form = QuestionAnswerForm()
    if form.validate_on_submit():
        new_que = QuestionAnswer(question = form.question.data, answer = form.answer.data)
        session.add(new_que)
        session.commit()
        return redirect(url_for('admin.about'))
    return render_template('admin_about_page/admin_about_que.html', form=form)

@admin.route('/dashboard/səhifələr/haqqımızda/Sual-Cavab/redaktə-et/<int:id>', methods = ['GET', 'POST'])
def about_que_edit(id):
    selectedData = session.query(QuestionAnswer).get(id)
    form = QuestionAnswerForm()
    if form.validate_on_submit():
        selectedData.question = form.question.data
        selectedData.answer = form.answer.data
        session.commit()
        return redirect(url_for('admin.about'))
    elif request.method == 'GET':
        form.question.data = selectedData.question
        form.answer.data = selectedData.answer
    return render_template('admin_about_page/admin_about_que.html', form=form)

@admin.route('/dashboard/səhifələr/haqqımızda/Sual-Cavab/sil/<int:id>', methods = ['GET'])
def about_que_delete(id):
    selectedData = session.query(QuestionAnswer).get(id)
    session.delete(selectedData)
    session.commit()
    return redirect(url_for('admin.about'))

# <--------------------------------------- Admin Advantages Page --------------------------------------------------------->

@admin.route('/dashboard/səhifələr/üstünlüklər', methods=['GET', 'POST'])
def advantages():
    form = SinglePageBannerImgForm()
    advantages = session.query(Advantage).all()
    selectedBanner = session.query(BannerImg).get(2)
    if form.validate_on_submit():
        if form.banner_img.data:
            uploaded_banner_file = request.files['banner_img']
            banner_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], banner_filename))
            selectedBanner.banner_img = banner_filename
            session.commit()
        return redirect(url_for('user.advantages'))
    return render_template('admin_advantages_page/admin_advantages.html', form=form, advantages=advantages)

@admin.route('/dashboard/səhifələr/üstünlüklər/əlavə-et', methods = ['GET', 'POST'])
def advantage_add():
    form = CardForm()
    if form.validate_on_submit():
        uploaded_file = request.files['card_img']
        svg_file = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], svg_file))

        new_adv = Advantage(svg_img = svg_file, title = form.title.data, description = form.description.data)
        session.add(new_adv)
        session.commit()
        return redirect(url_for('admin.advantages'))
    return render_template('admin_card_add.html', form=form)

@admin.route('/dashboard/səhifələr/üstünlüklər/redaktə-et/<int:id>', methods = ['GET', 'POST'])
def advantage_edit(id):
    form = CardForm()
    selectedAdv = session.query(Advantage).get(id)
    if form.validate_on_submit():
        if form.card_img.data:
            uploaded_banner_file = request.files['card_img']
            svg_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], svg_filename))
            selectedAdv.svg_img = svg_filename
        selectedAdv.title = form.title.data
        selectedAdv.description = form.description.data
        session.commit()
        return redirect(url_for('admin.advantages'))
    elif request.method == 'GET':
        form.title.data = selectedAdv.title
        form.description.data = selectedAdv.description
    return render_template('admin_card_add.html', form=form)

@admin.route('/dashboard/səhifələr/üstünlüklər/sil/<int:id>', methods = ['GET'])
def advantage_delete(id):
    selectedAdv = session.query(Advantage).get(id)
    session.delete(selectedAdv)
    session.commit()
    return redirect(url_for('admin.advantages'))

# <--------------------------------------- Admin Training Packages Page --------------------------------------------------------->

@admin.route('/dashboard/səhifələr/tədris-paketləri', methods=['GET', 'POST'])
def packages():
    form = SinglePageBannerImgForm()
    packages = session.query(Package).all()
    selectedBanner = session.query(BannerImg).get(3)
    if form.validate_on_submit():
        if form.banner_img.data:
            uploaded_banner_file = request.files['banner_img']
            banner_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], banner_filename))
            selectedBanner.banner_img = banner_filename
            session.commit()
        return redirect(url_for('user.packages'))
    return render_template('admin_packages_page/admin_packages.html', form=form, packages=packages)

@admin.route('/dashboard/səhifələr/tədris-paketləri/əlavə-et', methods = ['GET', 'POST'])
def package_add():
    form = CardForm()
    if form.validate_on_submit():
        uploaded_file = request.files['card_img']
        pack_file = secure_filename(uploaded_file.filename)

        new_pack = Package(pack_img = pack_file, title = form.title.data, description = form.description.data)
        session.add(new_pack)
        session.commit()
        return redirect(url_for('admin.packages'))
    return render_template('admin_card_add.html', form=form)

@admin.route('/dashboard/səhifələr/tədris-paketləri/redaktə-et/<int:id>', methods = ['GET', 'POST'])
def package_edit(id):
    form = CardForm()
    selectedPack = session.query(Package).get(id)
    if form.validate_on_submit():
        if form.card_img.data:
            uploaded_banner_file = request.files['card_img']
            pack_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], pack_filename))
            selectedPack.pack_img = pack_filename
        selectedPack.title = form.title.data
        selectedPack.description = form.description.data
        session.commit()
        return redirect(url_for('admin.packages'))
    elif request.method == 'GET':
        form.title.data = selectedPack.title
        form.description.data = selectedPack.description
    return render_template('admin_card_add.html', form=form)

@admin.route('/dashboard/səhifələr/tədris-paketləri/sil/<int:id>', methods = ['GET'])
def package_delete(id):
    selectedPack = session.query(Package).get(id)
    session.delete(selectedPack)
    session.commit()
    return redirect(url_for('admin.packages'))

# <--------------------------------------- Admin Admission Process Page --------------------------------------------------------->

@admin.route('/dashboard/səhifələr/qəbul-prosesi', methods=['GET', 'POST'])
def admission():
    form = SinglePageBannerImgForm()
    stages = session.query(AdmissionStage).all()
    selectedBanner = session.query(BannerImg).get(4)
    if form.validate_on_submit():
        if form.banner_img.data:
            uploaded_banner_file = request.files['banner_img']
            banner_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], banner_filename))
            selectedBanner.banner_img = banner_filename
            session.commit()
        return redirect(url_for('user.admission_process'))
    return render_template('admin_admission_page/admin_admission.html', form=form, stages=stages)

@admin.route('/dashboard/səhifələr/qəbul-prosesi/əlavə-et', methods = ['GET', 'POST'])
def admission_stage_add():
    form = CardForm()
    if form.validate_on_submit():
        uploaded_file = request.files['card_img']
        stage_file = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], stage_file))

        new_pack = AdmissionStage(stage_img = stage_file, title = form.title.data, description = form.description.data)
        session.add(new_pack)
        session.commit()
        return redirect(url_for('admin.admission'))
    return render_template('admin_card_add.html', form=form)

@admin.route('/dashboard/səhifələr/qəbul-prosesi/redaktə-et/<int:id>', methods = ['GET', 'POST'])
def admission_stage_edit(id):
    form = CardForm()
    selectedStage = session.query(AdmissionStage).get(id)
    if form.validate_on_submit():
        if form.card_img.data:
            uploaded_banner_file = request.files['card_img']
            stage_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], stage_filename))
            selectedStage.stage_img = stage_filename
        selectedStage.title = form.title.data
        selectedStage.description = form.description.data
        session.commit()
        return redirect(url_for('admin.admission'))
    elif request.method == 'GET':
        form.title.data = selectedStage.title
        form.description.data = selectedStage.description
    return render_template('admin_card_add.html', form=form)

@admin.route('/dashboard/səhifələr/qəbul-prosesi/sil/<int:id>', methods = ['GET'])
def admission_stage_delete(id):
    selectedStage = session.query(AdmissionStage).get(id)
    session.delete(selectedStage)
    session.commit()
    return redirect(url_for('admin.admission'))