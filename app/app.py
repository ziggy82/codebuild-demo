from flask import Flask

app = Flask(__name__)


@app.route("/health_check")
def health_check():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5151)
