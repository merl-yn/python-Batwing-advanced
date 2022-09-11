from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/<a>/<b>")
def sum_var(a, b):
    c = int(a) + int(b)
    return render_template("index.html", variable=c)


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
