from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = f"<h1>Hello World! Its the dawn of a new beginning</h1>"
    return html

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3000)
