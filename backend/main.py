from flask import Flask, request
import json

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

"""
Transcript endpoint
"""
@app.route('/transcript', methods=['GET', 'POST'])
def transcript():
    petitioner = request.form.get("petitionerValue")
    respondent = request.form.get("respondentValue")
    if (petitioner == "Sai" and respondent == "Merneedi"):
        return {'result': 'no its prathinav'}
    return {'result': 'tbd'}