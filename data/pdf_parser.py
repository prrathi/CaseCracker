import pandas as pd
import PyPDF4
import re
import itertools
import csv

sample = 'transcripts/2000/00-24.pdf'
pdfFileObj = open(sample, 'rb')
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

if pdfReader.isEncrypted:
    pdfReader.decrypt('')

# get page 0, process it separately to get names of appearances
pageObj0 = pdfReader.getPage(0)
startPage = pageObj0.extractText()
startPageLines = startPage.split('\n')
startPageLines2 = [line[3:] for line in startPageLines]
resultPage = ' '.join(startPageLines2)

# split into words for names
words = resultPage.split(' ')
wordsMod = [word for word in words if word.strip() != '']
start = False
afterStart = True
names = []
current = ""
for word in wordsMod:
    if word == "APPEARANCES:":
        start = True
    elif start and afterStart:
        if word == word.upper() and word.find(",") != -1:
            names.append(word[:-1])
            afterStart = False
    elif start:
        if word != word.upper():
            afterStart = True
        # elif current != "":
            # if word.find(".") == -1:
                # current = current[:-1]
                # names.append(current)
                # current = ""
            # else:
                # current = ""

# gives us the last names of petitioners/respondents who are in transcript
print(names)

# get page 2, and combine with rest of pages as one Page object
# page 1 has table contents and no actual transcript excerpts that would help us
pageObj = pdfReader.getPage(2)

for i in range(3, pdfReader.getNumPages()):

    # get each additional page
    pageObj2 = pdfReader.getPage(i)
    pageObj.mergePage(pageObj2)

# get entire page as one big string
page1 = pageObj.extractText()
# print(page1)

# split into lines and trim of first characters
pageLines = page1.split('\n')
pageLines2 = [line[3:] for line in pageLines]
# print(' '.join(pageLines2))

results = ' '.join(pageLines2)
finalWords = results.split(' ')
res1 = "".join(re.split("[^a-zA-Z ]*", results))

# to make new list with each entry corresponding to original names
totalNameWords = []
for _ in names:
    totalNameWords.append("")

# this is the other category outside of the names 
names.append("QUESTION")

res2 = re.split("({})".format("|".join(re.escape(n) for n in names)), res1)
res3 = ["".join(x) for x in itertools.zip_longest([""] + res2[1::2], res2[::2], fillvalue='')]
# print(len(res3))

# extract the content of speeches for person, add it to according position in our new list
for speech in res3:
    for i in range(len(names)-1):
        if(speech[:speech.find(" ")] == names[i]):
            totalNameWords[i] += speech[speech.find(" ")+1:]
            break
    
# filter out other irrelevant words
for i in range(len(totalNameWords)):
    separateWords = totalNameWords[i].split(' ')
    totalNameWords[i] = ' '.join([word for word in separateWords if not word.isupper()])

# write the files for future reference
# will be writing all them in the future as rows part of a larger dataframe
with open("names.txt", "w") as f:
    for n in names:
        f.write(str(n) +"\n")

with open("totalWords.txt", "w") as f:
    for n in totalNameWords:
        f.write(str(n) +"\n\n\n\n")