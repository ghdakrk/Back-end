from flask import Flask, render_template, Blueprint, session, redirect
from functools import wraps


app = Flask(__name__)
app.secret_key = b'\x8a\x12+\xd5\xaf\xf8\xc6\xf9{U\x8eI\x8e\x0c\xb3\xaa'


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    
    return wrap

# Routes
# app.register_blueprint(user_info)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index2')
def home2():
    return render_template('index2.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')    

if __name__ == '__main__':
    app.run(debug=True)
