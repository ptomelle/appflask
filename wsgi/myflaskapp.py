from flask import Flask,request, send_from_directory

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index.html")
def hello1():
    return send_from_directory('.', 'index.html')

@app.route("/index.html")
def hello2():
    return send_from_directory('/static/', 'index1.html')


if __name__ == "__main__":
    app.run()
