from flask import Flask, render_template, redirect, url_for, request, session, abort, flash
from .Inference.Inference import inference

from app import app
MODEL_PATH='app/Inference/model.pkl' #app/Inference/model.pkl
FILE_PATH ='app/Inference/cleaned_data.csv'

@app.route('/recommend/<userid>')
def get_recommendation_by_userid(userid:int):
    #return "userId is: {}, movie: x,y,z".format(userid)
    return inference(MODEL_PATH,FILE_PATH,UID = userid)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('Successful login.')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))
