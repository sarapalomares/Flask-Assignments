from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def numCounter():
	session['count'] += 1
	return render_template("index.html")

app.run(debug=True)
