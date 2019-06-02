from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
	html = "<h2>Hello World</h2>"
	return html

@app.route("/tester")
def tester():
	html = "<h2>Yo!</h2>"
	return html

if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 50)