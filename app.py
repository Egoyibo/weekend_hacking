from flask import Flask , render_template

app = Flask (__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/babaafrik")
def static_tunde():
	return render_template("tunde.html")


if __name__ == "__main__":
	app.run(host="0.0.0.0")
