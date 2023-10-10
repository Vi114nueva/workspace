from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import os

dbdir = 'sqlite:///' + os.path.abspath(os.getcwd()) + '/database.db' 

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.app_context().push()

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    description = db.Column(db.String(122))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return 'Welcome'
        else:
            return 'Incorrect credentials. Try again'
        
    return render_template('login.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        description = request.form['description']
        
        new_user = User(username=username, password=password, description=description)
        db.session.add(new_user)
        db.session.commit()
        
        return 'You are registered.'
    
    return render_template('signup.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        nickname = request.form['nickname']
        user = User.query.filter_by(username=nickname).first()
        if user:
            return f'Nickname: {user.username} <br> Description: {user.description}'
        else:
            return 'No user with that name was found.'
    
    return render_template('search.html')
    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)