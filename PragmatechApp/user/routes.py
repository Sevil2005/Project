from flask import Flask, render_template, url_for, Blueprint
from PragmatechApp.models import session, AboutPage, QuestionAnswer, Advantage, BannerImg, Package, AdmissionStage

user = Blueprint('user', __name__, template_folder="templates")

@user.route('/')
@user.route('/əsas-səhifə')
def index():
    return render_template('home.html')

@user.route('/haqqımızda')
def about():
    questions = session.query(QuestionAnswer).all()
    datas = session.query(AboutPage).get(1)
    banner_file = url_for('static', filename='user_assets/images/site_pics/' + datas.banner_img)
    second_file = url_for('static', filename='user_assets/images/site_pics/' + datas.second_img)
    return render_template('about.html', datas=datas, banner_file=banner_file, second_file=second_file, questions=questions)

@user.route('/üstünlüklər')
def advantages():
    advantages = session.query(Advantage).all()
    selectedBanner = session.query(BannerImg).get(2)
    banner_file = url_for('static', filename='user_assets/images/site_pics/' + selectedBanner.banner_img)
    return render_template('advantages.html', banner_file=banner_file, advantages=advantages)

@user.route('/tədris-paketləri')
def packages():
    packages = session.query(Package).all()
    selectedBanner = session.query(BannerImg).get(3)
    banner_file = url_for('static', filename='user_assets/images/site_pics/' + selectedBanner.banner_img)
    return render_template('training_packages.html', banner_file=banner_file, packages=packages)

@user.route('/qəbul-prosesi')
def admission_process():
    stages = session.query(AdmissionStage).all()
    selectedBanner = session.query(BannerImg).get(4)
    banner_file = url_for('static', filename='user_assets/images/site_pics/' + selectedBanner.banner_img)
    return render_template('admission_process.html', banner_file=banner_file, stages=stages)