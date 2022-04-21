from urllib import response
from flask import Flask, request
from flask_cors import CORS, cross_origin
import functions
import json
from nltk.corpus import stopwords
stopwords.words('english')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import gensim
from gensim import models, corpora
from gensim.parsing.preprocessing import preprocess_string
import pickle

vader = SentimentIntensityAnalyzer()
with open('../data/nlp/classify_model.pkl', 'rb') as f:
    classify_model = pickle.load(f)
with open('../data/nlp/dict.pkl', 'rb') as f:
    dictionary = pickle.load(f)
with open('../data/nlp/tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)
corpus = corpora.MmCorpus('../data/nlp/corpus.mm')
model = models.LsiModel(corpus, num_topics = 800)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'


@app.route('/')
@cross_origin()
def hello():
    return 'Hello, World!'


"""
Survey endpoint
"""
@app.route('/survey', methods=['POST'])
@cross_origin()
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
@cross_origin()
# clean input similar to the pdfs and then send predictions from trained models to frontend
def transcript():
    petitioner = request.json["petitionerValue"]
    respondent = request.json["respondentValue"]
    for i in range(2):
        if i == 0:
            text = petitioner
        if i == 1:
            text = respondent
        split = text.split(' ')
        tokens = [t for t in split]
        clean_tokens = []
        for i in range(len(tokens)):
            token = tokens[i]
            if re.search('[a-zA-Z]', token) and token not in stopwords.words('english'):
                token = re.sub(' +', ' ', token)
                clean_tokens.append(token)
        if i == 0:
            petitioner = ' '.join(clean_tokens)
        if i == 1:
            respondent = ' '.join(clean_tokens)

    polarity = vader.polarity_scores(respondent)['compound'] - vader.polarity_scores(petitioner)['compound']
    processed_res = dictionary.doc2bow(preprocess_string(respondent))
    processed_pet = dictionary.doc2bow(preprocess_string(petitioner))
    tfidf_corpus = tfidf[[processed_pet, processed_res]]
    vals1 = [item[1] for item in model[tfidf_corpus[0]]]
    vals2 = [item[1] for item in model[tfidf_corpus[1]]]
    output = [vals1[i] - vals2[i] for i in range(800)]
    output.append(polarity)
    result = classify_model.predict_proba([output])

    return {'result': result[0][1]} 