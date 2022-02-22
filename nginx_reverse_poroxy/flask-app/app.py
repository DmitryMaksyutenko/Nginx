from flask import Flask


app = Flask(__name__)


@app.route("/")
def main_page():
    return '<p>Flask main page.</p>'

@app.route("/page1")
def page_1():
    return '<p>Flask Page one.</p>'
