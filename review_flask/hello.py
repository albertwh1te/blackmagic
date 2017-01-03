from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/user/<name>')
def hi_user(name):
    return render_template('hi.html', name=name)


if  __name__ == "__main__":
    app.run(debug=True)
