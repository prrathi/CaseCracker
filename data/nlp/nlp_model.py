from dataclasses import replace
from operator import index
from tabnanny import verbose
from bleach import clean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
stopwords.words('english')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import date
import re
import gensim
from gensim import models, corpora
from gensim.parsing.preprocessing import preprocess_documents
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=DeprecationWarning)

dfClean = pd.read_csv("clean_final.csv", encoding = 'unicode_escape', engine ='python')
dfTarget = pd.read_csv("SCDB_filtered2.csv", encoding = 'unicode_escape', engine ='python')

numrows = dfClean.shape[0]

# compute the polarity score given a dataframe and the two column names to compare, returns a list
def polarityScore(df, cols):
    vader = SentimentIntensityAnalyzer()
    polarity = []
    for i in range(df.shape[0]):
        col0 = 0
        col1 = 0
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

# maps each court case to the ultimate result, whether petitioner or respondent won
def targetData(dfTarget, df):
    target = []
    remove_index = []
    id = df["ID"]
    for i in range(len(id)):
        label = id.iloc[i]
        if '.' in label:
            label = label.replace('.', '')
        res = dfTarget[dfTarget.docket == label]
        if (res.shape[0] == 0):
            remove_index.append(i)
        else:
            target.append(res.iloc[0, 1])
    return target, remove_index

# FIRST TIME THROUGH:
# run the polarity function and save as csv to reduce future computational time
# create the corpus and save into gensim-native mm file

# cols = ["Petitioner", "Respondent"]

# dfOutput = pd.DataFrame(index=range(dfClean.shape[0]), columns=["Polarity"])
# polarityCol = polarityScore(dfClean, cols)
# dfOutput["Polarity"] = pd.Series(polarityCol)
# dfOutput.to_csv("polarity.csv", index=False)
# print("finished polarity")

# corpus = convertCorpus(dfClean, cols)
# corpora.MmCorpus.serialize('./corpus.mm', corpus)

# target, remove_index = targetData(dfTarget, dfClean)
# dfClean.drop(remove_index, inplace=True)
# dfClean.insert(loc=0, column='Outcome', value=target)
# dfClean.to_csv("clean_final.csv", index=False)

# AFTER FIRST TIME THROUGH:
# load files created above in for use
dfOutput = pd.read_csv("polarity.csv")
polarity = dfOutput.Polarity
corpus = corpora.MmCorpus('./corpus.mm')
actual = dfClean.Outcome

logacc = []
svmacc = []

# get training and testing splits by index, map the target variable accordingly
total_samples = np.arange(numrows)
train_samples = np.random.choice(numrows, numrows * 8 // 10, replace=False)
train_actual = actual[train_samples]
train_actual = train_actual.values
train_polarity = polarity[train_samples]
train_polarity = train_polarity.values

mask = np.in1d(total_samples, train_samples)
test_samples = np.where(~mask)[0]
test_actual = actual[test_samples]
test_actual = test_actual.values
test_polarity = polarity[test_samples]
test_polarity = test_polarity.values


# train model using training split, test using testing split, iterated from 100 to 800 latent variables
# determine accuracy on testing split based on original target, using logistic regression and support vector machine
"""for topic in range(100, 850, 50):
    print("number of latent variables: ", topic)
    model = models.LsiModel(corpus, num_topics = topic)
    train_dfLsi = pd.DataFrame(columns = range(topic))
    count = 0
    for i in train_samples:
        petitioner = [item[1] for item in model[corpus[i]]]
        respondent = [item[1] for item in model[corpus[i + numrows]]]
        train_dfLsi.loc[count] = [petitioner[i] - respondent[i] for i in range(len(petitioner))]
        count += 1
    train_dfLsi = train_dfLsi.assign(Polarity = train_polarity)
    logreg = LogisticRegression()
    # print(train_dfLsi)
    # print(train_actual)
    logreg.fit(train_dfLsi, train_actual)
    svm = LinearSVC()
    svm.fit(train_dfLsi, train_actual)
    test_dfLsi = pd.DataFrame(columns = range(topic))
    count = 0
    for i in test_samples:
        petitioner = [item[1] for item in model[corpus[i]]]
        respondent = [item[1] for item in model[corpus[i + numrows]]]
        test_dfLsi.loc[count] = [petitioner[i] - respondent[i] for i in range(len(petitioner))]
        count += 1
    test_dfLsi = test_dfLsi.assign(Polarity = test_polarity)
    acc = logreg.score(test_dfLsi, test_actual)
    logacc.append(acc)
    print("logistic regression test accuracy: ", acc)
    acc = svm.score(test_dfLsi, test_actual)
    svmacc.append(acc)
    print("support vector machine test accuracy: ", acc)
    print()
"""
# 66% accuracy reached at certain # like 500


# try a neural network with dense layers, using the 500-sized LSI model
model = models.LsiModel(corpus, 500)
# train_dfLsi = pd.DataFrame(columns = range(500))
# count = 0
# for i in train_samples:
    # petitioner = [item[1] for item in model[corpus[i]]]
    # respondent = [item[1] for item in model[corpus[i + numrows]]]
    # train_dfLsi.loc[count] = [petitioner[i] - respondent[i] for i in range(len(petitioner))]
    # count += 1
# train_dfLsi = train_dfLsi.assign(Polarity = train_polarity)

# test_dfLsi = pd.DataFrame(columns = range(500))
# count = 0
# for i in test_samples:
    # petitioner = [item[1] for item in model[corpus[i]]]
    # respondent = [item[1] for item in model[corpus[i + numrows]]]
    # test_dfLsi.loc[count] = [petitioner[i] - respondent[i] for i in range(len(petitioner))]
    # count += 1
# test_dfLsi = test_dfLsi.assign(Polarity = test_polarity)

# use k-fold cross validation instead of the 80/20 split from above 
dfLsi = pd.DataFrame(columns=range(500))
for i in range(numrows):
    petitioner = [item[1] for item in model[corpus[i]]]
    respondent = [item[1] for item in model[corpus[i + numrows]]]
    dfLsi.loc[i] = [petitioner[i] - respondent[i] for i in range(len(petitioner))]
dfLsi = dfLsi.assign(Polarity = polarity)

def create_model():
    model = Sequential()
    model.add(Dense(501, input_dim=501, activation = 'relu'))
    model.add(Dense(350, activation = 'relu'))
    model.add(Dense(250, activation = 'relu'))
    model.add(Dense(200, activation = 'relu'))
    model.add(Dense(150, activation = 'relu'))
    model.add(Dense(100, activation = 'relu'))
    model.add(Dense(60, activation = 'relu'))
    model.add(Dense(30, activation = 'relu'))
    model.add(Dense(10, activation = 'relu'))
    model.add(Dense(1, activation = 'sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasClassifier(build_fn=create_model, epochs=5, batch_size=1, verbose=0)))
pipeline = Pipeline(estimators)
kfold = StratifiedKFold(n_splits=5, shuffle=True)
results = cross_val_score(pipeline, dfLsi, actual, cv=kfold)
print("Accuracy and deviation: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
# 64% accuracy

# model.fit(train_dfLsi, train_actual, epochs = 5, batch_size = 1, verbose=1)
# model.summary()

# score = model.evaluate(test_dfLsi, test_actual, verbose=1)
# print(score) 