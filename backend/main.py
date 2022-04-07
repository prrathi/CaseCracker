rom flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


"""
Survey endpoint
"""
@app.route('/survey', methods=['POST'])
def survey():
    # print(request.json)

    return request.json