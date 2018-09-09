from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/class')
def class_info():
    return render_template("class_information.html")


if __name__ == '__main__':
    app.run()
