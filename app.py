import praser
from flask import Flask, flash, render_template, request

app = Flask(__name__, template_folder='templates/')
app.secret_key = "Iniyan2006"
@app.route('/')
def home():
	flash(praser.text())
	return render_template('home.html')
@app.route("/joke")
def joke():
	flash(praser.text())
	return render_template('home.html')
if __name__ == "__main__":	
	app.run(debug=True)
