from flask import Flask, render_template, redirect, request, session, flash
import re

from mysqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'emailval_wDB')
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
    else:
        query = "INSERT INTO user (email, created_at) VALUES (:email, NOW())"
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        return redirect ('/emailshow')
    return redirect ('/')

@app.route('/emailshow')
def show():
    query = "SELECT * FROM email"
    email = mysql.query_db(query)
    return render_template('success.html', email=email, session=session['session'])

app.run(debug=True)
