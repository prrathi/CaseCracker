from operator import index
from bleach import clean
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
stopwords.words('english')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import date
import re
import gensim
from gensim import models
from gensim.parsing.preprocessing import preprocess_documents
from sklearn.linear_model import LogisticRegression

dfClean = pd.read_csv("transcripts_clean2.csv", encoding = 'unicode_escape', engine ='python')

columns = ["Polarity", "LearnedSentiment"] #ADD MORE LATER
dfOutput = pd.DataFrame(index=range(dfClean.shape[0]), columns=["Polarity"])

numrows = dfClean.shape[0]

def polarityScore(df, cols):
    vader = SentimentIntensityAnalyzer()
    polarity = []
    for i in range(df.shape[0]):
        col0 = 0
        col1 = 0
        print(df[cols[0]])
        if (df[cols[0]][i] != ' '):
            col0 = vader.polarity_scores(df[cols[0]][i])['compound'] 
        if (df[cols[1]][i] != ' '):
            col1 = vader.polarity_scores(df[cols[1]][i])['compound']
        polarity.append(col1 - col0)
    return polarity

def convertCorpus(df, col):
    corpus = df[col].values
    processed_corpus = preprocess_documents(corpus)
    dict_corpus = [gensim.corpora.Dictionary(processed_corpus).doc2bow(text) for text in processed_corpus]
    tfidf = gensim.models.TfidfModel(dict_corpus, smartirs='nfc')
    tfidf_corpus = tfidf[dict_corpus]
    return tfidf_corpus

cols = ["Petitioner", "Respondent"]

# polarityCol = polarityScore(dfClean, cols)
# dfOutput["Polarity"] = pd.Series(polarityCol)
# dfOutput.to_csv("polarity.csv")
# print("finished polarity")

petCorpus = convertCorpus(dfClean, "Petitioner")
resCorpus = convertCorpus(dfClean, "Respondent")

for topic in range(50, 500, 50):
    model = models.LsiModel(petCorpus, num_topics = topic)
    dfLsi = pd.DataFrame(columns = range(topic))
    for i in range(numrows):
        dfLsi.loc[len(dfLsi.index)] = [item[1] for item in model[petCorpus[i]]]
    # ONCE WE GET THE BINARY FOR WHICH SIDE WON
    logreg = LogisticRegression()
    logreg.fit(dfLsi, actual)
    acc = logreg.score(dfLsi, actual)
    print("number of latent variables: ", topic)
    print("accuracy: ", acc)
    print()

    break # comment out later

print("finished lsi")

"""
for num_topic in range(50, 1000, 50):
    print(num_topic)
    lsi = gensim.models.LsiModel(tfidf_corpus, num_topics=num_topic)
    index = gensim.similarities.MatrixSimilarity(lsi[tfidf_corpus])
    corpus_lsi = lsi[tfidf_corpus]
    results = index[corpus_lsi]

    # results for each of the num_topic possibilities
    print(results)
    print()
    # for s in sorted(enumerate(results), key=lambda item: -item[1]):
        # print(s[0])
        # print(s[1])
    # for text in df["Sample2"]:
        # print(lsi[text])
"""