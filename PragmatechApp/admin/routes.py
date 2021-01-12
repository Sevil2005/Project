import os
from flask import Flask, render_template, url_for, redirect, request, Blueprint
from PragmatechApp import app, user
from PragmatechApp.models import session, AboutPage, QuestionAnswer, Advantage, BannerImg, Package, GuarantiesPage
from PragmatechApp.admin.forms import BannerImgForm, AboutPageForm, QuestionAnswerForm, CardForm, SinglePageBannerImgForm, GuarantiesForm, PackageForm
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

@admin.route('/dashboard/səhifələr/haqqımızda', methods=['GET', 'POST'])
def about():
    datas = session.query(AboutPage).all()
    questions = session.query(QuestionAnswer).all()
    form = SinglePageBannerImgForm()
    if session.query(AboutPage).get(1):
        pass
    else:
        details = AboutPage(main_text = "Default Text", second_img = "defolt.jpg")
        session.add(details)
        session.commit()
    selectedBanner = session.query(BannerImg).get(1)
    if form.validate_on_submit():
        if form.banner_img.data:
            uploaded_banner_file = request.files['banner_img']
            banner_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], banner_filename))
            selectedBanner.banner_img = banner_filename
            session.commit()
        return redirect(url_for('user.about'))
    return render_template('admin_about_page/admin_about.html', form=form, datas=datas, banner_img=selectedBanner, questions=questions)

@admin.route('/dashboard/səhifələr/haqqımızda/Banner-Section/redaktə-et', methods = ['GET', 'POST'])
def about_edit():
    form = AboutPageForm()
    selectedData = session.query(AboutPage).get(1)
    if form.validate_on_submit():
        if form.second_img.data:
            uploaded_second_file = request.files['second_img']
            second_filename = secure_filename(uploaded_second_file.filename)
            uploaded_second_file.save(os.path.join(app.config['UPLOAD_PATH'], second_filename))
            selectedData.second_img = second_filename
        
        selectedData.main_text = form.main_text.data
        session.commit()
        return redirect(url_for('user.about'))
    elif request.method == 'GET':
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
    return render_template('admin_advantages_page/admin_advantages.html', form=form, banner_img=selectedBanner, advantages=advantages)

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
    return render_template('admin_packages_page/admin_packages.html', form=form, banner_img=selectedBanner, packages=packages)

@admin.route('/dashboard/səhifələr/tədris-paketləri/əlavə-et', methods = ['GET', 'POST'])
def package_add():
    form = PackageForm()
    if form.validate_on_submit():
        uploaded_file = request.files['pack_img']
        pack_file = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], pack_file))

        new_pack = Package(pack_img = pack_file, title = form.title.data, description = form.description.data, all_details = form.all_details.data)
        session.add(new_pack)
        new_banner = BannerImg(banner_img = "defolt.jpg", page_name = form.title.data)
        session.add(new_banner)
        session.commit()
        return redirect(url_for('admin.packages'))
    return render_template('admin_packages_page/admin_package_add.html', form=form)

@admin.route('/dashboard/səhifələr/tədris-paketləri/redaktə-et/<int:id>', methods = ['GET', 'POST'])
def package_edit(id):
    form = PackageForm()
    bannerForm = SinglePageBannerImgForm()
    selectedPack = session.query(Package).get(id)
    if form.validate_on_submit():
        if form.pack_img.data:
            uploaded_banner_file = request.files['pack_img']
            pack_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], pack_filename))
            selectedPack.pack_img = pack_filename
        selectedPack.title = form.title.data
        selectedPack.description = form.description.data
        selectedPack.all_details = form.all_details.data
        session.commit()
        return redirect(url_for('admin.packages'))
    selectedBanner = session.query(BannerImg).get(3)
    selectedPackBanner = session.query(BannerImg).filter_by(page_name=selectedPack.title).first()
    if bannerForm.validate_on_submit():
        if bannerForm.banner_img.data:
            uploaded_banner_file = request.files['banner_img']
            banner_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], banner_filename))
            selectedPackBanner.banner_img = banner_filename
            session.commit()
        return redirect(url_for('user.packages'))
    elif request.method == 'GET':
        form.title.data = selectedPack.title
        form.description.data = selectedPack.description
        form.all_details.data = selectedPack.all_details
    return render_template('admin_packages_page/admin_package_edit.html', form=form, bannerForm=bannerForm, banner_img=selectedPackBanner)

@admin.route('/dashboard/səhifələr/tədris-paketləri/sil/<int:id>', methods = ['GET'])
def package_delete(id):
    selectedPack = session.query(Package).get(id)
    session.delete(selectedPack)
    session.commit()
    return redirect(url_for('admin.packages'))

# <--------------------------------------- Admin Guaranties Page --------------------------------------------------------->

@admin.route('/dashboard/səhifələr/zəmanətlərimiz', methods=['GET', 'POST'])
def guaranties():
    form = SinglePageBannerImgForm()
    form_details = GuarantiesForm()
    selectedBanner = session.query(BannerImg).get(4)
    if session.query(GuarantiesPage).get(1) :
        pass
    else :
        details = GuarantiesPage(content = "Default Description")
        session.add(details)
        session.commit()
    PageDetails = session.query(GuarantiesPage).get(1)
    if form_details.validate_on_submit():
        PageDetails.content = form_details.content.data
        session.commit()
        return redirect(url_for('admin.guaranties'))
    if form.validate_on_submit():
        if form.banner_img.data:
            uploaded_banner_file = request.files['banner_img']
            banner_filename = secure_filename(uploaded_banner_file.filename)
            uploaded_banner_file.save(os.path.join(app.config['UPLOAD_PATH'], banner_filename))
            selectedBanner.banner_img = banner_filename
        session.commit()
        return redirect(url_for('admin.guaranties'))
    elif request.method == 'GET':
        form_details.content.data = PageDetails.content
    return render_template('admin_guaranties_page/admin_guaranties.html', form=form, form_details=form_details, details=PageDetails, banner_img=selectedBanner)
