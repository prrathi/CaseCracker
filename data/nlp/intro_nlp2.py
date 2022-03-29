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
from gensim import models, corpora
from gensim.parsing.preprocessing import preprocess_documents
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

dfClean = pd.read_csv("clean_final.csv", encoding = 'unicode_escape', engine ='python')

numrows = dfClean.shape[0]

# compute the polarity score given a dataframe and the two column names to compare, returns a list
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

# determine the corpus then used for nlp techniques given a dtaframe and the column name
def convertCorpus(df, cols):
    corpus = []
    for col in cols:
        corpus.extend(df[col].tolist())
    processed_corpus = preprocess_documents(corpus)
    dict_corpus = [gensim.corpora.Dictionary(processed_corpus).doc2bow(text) for text in processed_corpus]
    tfidf = gensim.models.TfidfModel(dict_corpus, smartirs='nfc')
    tfidf_corpus = tfidf[dict_corpus]
    return tfidf_corpus


# dfOutput = pd.DataFrame(index=range(dfClean.shape[0]), columns=["Polarity"])
# polarityCol = polarityScore(dfClean, cols)
# dfOutput["Polarity"] = pd.Series(polarityCol)
# dfOutput.to_csv("polarity.csv")
# print("finished polarity")

# first time through:
# cols = ["Petitioner", "Respondent"]
# corpus = convertCorpus(dfClean, cols)
# corpora.MmCorpus.serialize('./corpus.mm', corpus)
corpus = corpora.MmCopus('./corpus.mm')

# ONCE WE GET THE BINARY FOR WHICH SIDE WON
for topic in range(50, 500, 50):
    print("number of latent variables: ", topic)
    model = models.LsiModel(corpus, num_topics = topic)
    dfLsi = pd.DataFrame(columns = range(topic))
    for i in range(numrows):
        petitioner = [item[1] for item in model[corpus[i]]]
        respondent = [item[1] for item in model[corpus[i + numrows]]]
        dfLsi.loc[len(dfLsi.index)] = [petitioner[i] - respondent[i] for i in range(len(petitioner))]
    logreg = LogisticRegression()
    logreg.fit(dfLsi, actual)
    acc = logreg.score(dfLsi, actual)
    print("logistic accuracy: ", acc)

    svm = SVC(kernel = 'linear')
    svm.fit(dfLsi, actual)
    acc = svm.score(dfLsi, actual)
    print("support vector machine accuracy: ", acc)
    
    print()
    break # comment out later

print("finished lsi")
