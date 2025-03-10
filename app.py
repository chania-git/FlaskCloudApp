from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Hope! Your Flask app is working.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)