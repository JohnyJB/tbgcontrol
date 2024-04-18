from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "this is the home page"


def hello_world():
    return 'Hello World 3'


if __name__ == "__main__":
    app.run()
