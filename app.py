from flask import Flask, render_template
app = Flask(__name__, template_folder="static")

@app.route('/')
def hello():
	return render_template("index.html") 

@app.route('/ps4')
def ps4():
	return render_template("ps4.html") 

if __name__ == '__main__':
	app.run(debug=True)
