from http import HTTPStatus
from flask import Blueprint
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

auth_controller = Blueprint('auth', __name__)

@auth_controller.route('/login')
def login_controller():
    return 'hola'
