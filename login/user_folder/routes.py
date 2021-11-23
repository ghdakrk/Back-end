from flask import Flask, Blueprint
from user_folder.models import User

user_info = Blueprint('user_info', __name__)

@user_info.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@user_info.route('/user/signout')
def signout():
  return User().signout()

@user_info.route('/user/login', methods=['POST'])
def login():
  return User().login()