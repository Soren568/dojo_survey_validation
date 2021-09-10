from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.ninjas import Ninja

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    if not Ninja.validate_ninja(request.form):
        return redirect('/')
    Ninja.save(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('results.html')

@app.route('/home')
def return_home():
    return redirect('/')