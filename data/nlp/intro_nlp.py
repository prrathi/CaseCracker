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


# get naive polarity score using the sentiment analysis tool from nltk
# run the analysis of texts for each entry in the columm, this gives us overall sentiment for each speech given 

def cleanText(df, col):
    finalText = []
    count = 0
    for text in df[col]: # change to actual column name
        if (not pd.isna(text)):
            split = text.split(' ')
            tokens = [t for t in split]
            clean_tokens = []

            for i in range(len(tokens)):
                token = tokens[i]
                if re.search('[a-zA-Z]', token) and token not in stopwords.words('english'):
                    token = re.sub(' +', ' ', token)
                    clean_tokens.append(token)
            finalText.append(' '.join(clean_tokens))
        else:
            finalText.append(' ')
    return finalText

cols = ["Petitioner", "Respondent"]
for col in cols:
    cleanedCol = cleanText(df, col)
    dfClean[col] = pd.Series(cleanedCol)
dfClean.to_csv("transcripts_clean.csv", index=False)
