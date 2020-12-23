from flask import Flask, render_template, url_for, Blueprint

user = Blueprint('user', __name__, template_folder="templates")

@user.route('/')
@user.route('/əsas-səhifə')
def index():
    return render_template('layout.html')

@user.route('/haqqımızda')
def about():
    return render_template('about.html')