from flask import Flask


app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
