from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello world"
@app.route("/rufles")
def index():
	return "Hello ruffle"

if __name__ == "__main__":
	app.run()
