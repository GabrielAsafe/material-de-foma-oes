from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)



@app.route("/")
def index():
	return render_template("index.html")


@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		manuel = request.form['nm']
		return redirect(url_for('carlos', putas=manuel))
	else:

		return render_template("login.html")



@app.route("/<putas>")
def carlos(putas):
	return f"<h1>{putas}</h1>"

if __name__ == '__main__':
	app.run(debug=True)
