from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
import uuid
from pymongo import MongoClient
from werkzeug.utils import redirect

# Database
client = MongoClient('localhost', 27017)
db = client.user_login_system


class User:

    def start_session(self, user_info):
        del user_info['password']
        session['logged_in'] = True
        session['user_info'] = user_info
        return jsonify(user_info), 200



    def signup(self):
        print(request.form)

        # Create the user object
        user_info = {
            "_id":uuid.uuid4().hex,
            "name":request.form.get('name'),
            "email":request.form.get('email'),
            "password":request.form.get('password')
        }

        # Encrypt the password
        user_info['password'] = pbkdf2_sha256.encrypt(user_info['password'])

        # Check for existing email address
        if db.users.find_one({"email": user_info['email']}):
            return jsonify({"error" : "Email address already in user"}), 400

        if db.users.insert_one(user_info):
            return self.start_session(user_info)

        return jsonify({'error': 'Signup failed'}), 400
    
    def signout(self):
        session.clear()
        return redirect('/')

    
    def login(self):

        user_info = db.users.find_one({
            "email":request.form.get('email')
        })

        if user_info and pbkdf2_sha256.verify(request.form.get('password'), user_info['password']):
            return self.start_session(user_info)

        return jsonify({ "error": "Invalid login credentials"}), 401