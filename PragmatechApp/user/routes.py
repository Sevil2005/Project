from flask import Flask, render_template, url_for, Blueprint
from PragmatechApp.models import session, AboutPage, QuestionAnswer, Advantage, BannerImg, Package, GuarantiesPage

user = Blueprint('user', __name__, template_folder="templates")

@user.route('/')
@user.route('/əsas-səhifə')
def index():
    return render_template('home.html')

@user.route('/haqqımızda')
def about():
    questions = session.query(QuestionAnswer).all()
    datas = session.query(AboutPage).get(1)
    selectedBanner = session.query(BannerImg).get(1)
    banner_file = url_for('static', filename='user_assets/images/site_pics/' + selectedBanner.banner_img)
    second_file = url_for('static', filename='user_assets/images/site_pics/' + datas.second_img)
    return render_template('about.html', datas=datas, banner_file=banner_file, second_file=second_file, questions=questions)

@user.route('/üstünlüklər')
def advantages():
    advantages = session.query(Advantage).all()
    selectedBanner = session.query(BannerImg).get(2)
    banner_file = url_for('static', filename='user_assets/images/site_pics/' + selectedBanner.banner_img)
    return render_template('advantages.html', banner_file=banner_file, advantages=advantages)

@user.route('/zəmanətlərimiz')
def guaranties():
    details = session.query(GuarantiesPage).get(1)
    selectedBanner = session.query(BannerImg).get(4)
    banner_file = url_for('static', filename='user_assets/images/site_pics/' + selectedBanner.banner_img)
    return render_template('guaranties.html', banner_file=banner_file, details=details)

@user.route('/tədris-paketləri')
def packages():
    packages = session.query(Package).all()
    selectedBanner = session.query(BannerImg).get(3)
    banner_file = url_for('static', filename='user_assets/images/site_pics/' + selectedBanner.banner_img)
    return render_template('training_packages.html', banner_file=banner_file, packages=packages)

@user.route('/tədris-paketləri/<string:pack_name>')
def package_details(pack_name):
    if session.query(Package).filter_by(title=pack_name).first():
        package = session.query(Package).filter_by(title=pack_name).first()
        selectedBanner = session.query(BannerImg).filter_by(page_name=pack_name).first()
        banner_file = url_for('static', filename='user_assets/images/site_pics/' + selectedBanner.banner_img)
        return render_template('package_details.html', banner_file=banner_file, package=package)