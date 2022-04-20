from urllib import response
from flask import Flask, request
import functions

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

    responseValues = []

    print(request.json)

    for number in request.json['questions']:
        responseValues.append(number)

    averages = functions.findIssueAvg(responseValues)

    closestJusticeList = functions.findClosestJustice(averages)

    closestJustices = {
        "justices": closestJusticeList
    }

    return closestJustices

"""
Transcript endpoint
"""
@app.route('/Transcripts', methods=['GET', 'POST'])
def transcript():
    print(request)
    # petitioner = request.json["petitionerValue"]
    # respondent = request.json["respondentValue"]
    # print(petitioner)
    # print(respondent)
    # if (petitioner == "Sai" and respondent == "Merneedi"):
        # return {'result': 'no its prathinav'}
    return {'result': 'tbd'}