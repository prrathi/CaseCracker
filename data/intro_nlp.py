import pandas as pd
import time
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
stopwords.words('english')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import date
import gensim
from gensim.parsing.preprocessing import preprocess_documents


vader = SentimentIntensityAnalyzer()
df = pd.read_csv("sample.csv") #TODO: organize loaded data as dataframes with text composing one of columns

columns = ["NaiveSentiment", "LearnedSentiment"] #ADD MORE LATER
dfOutput = pd.DataFrame(columns=columns)

# counts occurrences of ticker symbols in comments
naive = []
corpus = df["Sample2"].values
for text in df["Sample2"]: # change to actual column name

    naive.append(vader.polarity_scores(text)['compound'])

    split = text.split(' ')
    tokens = [t for t in split]
    clean_tokens = tokens[:]

    for token in clean_tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)

processed_corpus = preprocess_documents(corpus)
dict_corpus = [gensim.corpora.Dictionary(processed_corpus).doc2bow(text) for text in processed_corpus]

tfidf = gensim.models.TfidfModel(dict_corpus, smartirs='nfc')
tfidf_corpus = tfidf[dict_corpus]

for num_topic in range(50, 1000, 50):
    print(num_topic)
    lsi = gensim.models.LsiModel(tfidf_corpus, num_topics=num_topic)
    index = gensim.similarities.MatrixSimilarity(lsi[tfidf_corpus])
    corpus_lsi = lsi[tfidf_corpus]
    results = index[corpus_lsi]
    print(results)
    print()
    # for s in sorted(enumerate(results), key=lambda item: -item[1]):
        # print(s[0])
        # print(s[1])
    # for text in df["Sample2"]:
        # print(lsi[text])

