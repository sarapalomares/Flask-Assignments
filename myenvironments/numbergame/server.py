from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if "random" in session:
		pass
	else:
		session['random'] = random.randrange(0, 101)
	if "guess" in session:
		return render_template('index.html', random=session['random'], guess=session['guess'])
	else:
		return render_template('index.html', random=session['random'])


@app.route('/submit', methods=["post"])
def user_guess():
	session['guess'] = int(request.form['number'])
	return redirect('/')

@app.route('/reset')
def clear():
	session.pop('random', 'guess')
	return redirect('/')

app.run(debug=True)
