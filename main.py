from flask import *
# from tkinter import *
# from tkinter import ttk


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/watermark")
def watermark():
    return render_template("watermark.html")


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
