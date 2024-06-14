from flask import Blueprint, render_template

Menu = Blueprint('MenuForm', __name__)

@Menu.route('/MenuForm')
def index():
    return render_template('Menu_Form.html')