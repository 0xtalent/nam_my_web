from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h5>헬로 파이썬</h5>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
