from flask import Flask, render_template, url_for, Blueprint

admin = Blueprint('admin', __name__, template_folder="templates")

@admin.route('/dashboard')
def index():
    return render_template('admin_layout.html')

@admin.route('/dashboard/səhifələr/haqqımızda')
def about():
    return render_template('pages/admin_about.html')