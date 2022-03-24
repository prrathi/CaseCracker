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
from gensim import models
from gensim.parsing.preprocessing import preprocess_documents


df = pd.read_csv("transcripts_new.csv", encoding = 'unicode_escape', engine ='python')
# df.dropna(how = 'all', inplace=True)
# df.to_csv("transcripts.csv", index=False)

dfClean = pd.DataFrame(index=range(df.shape[0]), columns = df.columns)
dfClean["Year"] = df["Year"]
dfClean["ID"] = df["ID"]

columns = ["clean", "LearnedSentiment"] #ADD MORE LATER
dfOutput = pd.DataFrame(index=range(df.shape[0]), columns=columns)

# get naive polarity score using the sentiment analysis tool from nltk
# run the analysis of texts for each entry in the columm, this gives us overall sentiment for each speech given 

def cleanText(df, col):
    finalText = []
    for text in df[col]: # change to actual column name

        split = text.split(' ')
        tokens = [t for t in split]
        clean_tokens = []

        for i in range(len(tokens)):
            token = tokens[i]
            if re.search('[a-zA-Z]', token) and token not in stopwords.words('english'):
                token = re.sub(' +', ' ', token)
                clean_tokens.append(token)

        finalText.append(' '.join(clean_tokens))
    return finalText

def polarityScore(df, cols):
    vader = SentimentIntensityAnalyzer()
    polarity = []
    for i in range(df.shape[0]):
        polarity.append(vader.polarity_scores(df[cols[1]][i])['compound'] - vader.polarity_scores(df[cols[0]][i])['compound'])
    return polarity

def convertCorpus(df, col):
    corpus = df[col].values
    processed_corpus = preprocess_documents(corpus)
    dict_corpus = [gensim.corpora.Dictionary(processed_corpus).doc2bow(text) for text in processed_corpus]
    tfidf = gensim.models.TfidfModel(dict_corpus, smartirs='nfc')
    tfidf_corpus = tfidf[dict_corpus]
    return tfidf_corpus

cols = ["Petitioner", "Respondent"]
for col in cols:
    cleanedCol = cleanText(df, col)
    dfClean[col] = pd.Series(cleanedCol)

polarityCol = polarityScore(dfClean, cols)
dfOutput[col] = pd.Series(polarityCol)

petCorpus = convertCorpus(dfClean, "Petitioner")
resCorpus = convertCorpus(dfClean, "Respondent")

model = models.LsiModel(petCorpus, num_topics = 50)
print(model[petCorpus[0]])

dfClean.to_csv("transcripts_clean.csv", index=False)

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