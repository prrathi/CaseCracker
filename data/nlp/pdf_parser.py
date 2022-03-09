import pandas as pd
import PyPDF4
import re
import itertools
import csv
import datetime

now = datetime.datetime.now()

transcripts = pd.read_csv('transcripts.csv').iloc[:,1:]
print(transcripts.columns)
def read_pdf(year, pdf_id, transcripts):

    sample = 'transcripts/' + year + '/' + pdf_id + '.pdf'
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
    end = False
    names = []
    for word in wordsMod:
        if word == "APPEARANCES:":
            start = True
        elif start and afterStart:
            # this is how we get the last names of people
            if word == word.upper() and word.find(",") != -1:
                names.append(word[:-1])
                afterStart = False
                end = True
        elif start:
            if word != word.upper():
                afterStart = True
        if end and word.find("1") != -1:
            # stop when page number is met
            break

    pageObj1 = pdfReader.getPage(1)
    startPage1 = pageObj1.extractText()
    words1 = startPage1.split('\n')[1][3:].split(' ')
    count = False

    # check if the second page has more people descriptions
    if 'APPEARANCES:' in words1:
        count = True
        startPageLines1 = startPage1.split('\n') 
        startLines1 = [line[3:] for line in startPageLines1]
        resultPage1 = ' '.join(startLines1)
        words1 = resultPage1.split(' ')
        wordsMod1 = [word for word in words1 if word.strip() != '']
        start = False
        afterStart = True
        end = False
        for word in wordsMod1:
            if word == "APPEARANCES:":
                start = True
            elif start and afterStart:
                # this is again how we get last names of people
                if word == word.upper() and word.find(",") != -1:
                    names.append(word[:-1])
                    end = True
                    afterStart = False
            elif start:
                if word != word.upper():
                    afterStart = True
            if end and word.find("2") != -1:
                # stop when page number is met
                break

    # names gives us the last names of petitioners/respondents who are in transcript
    # depending on whether or not the names extend to another page, we start on the following page

    # the following page would have labels for petitioner and respondent for each of the names, so we search through and get their labels   
    # the if else condition is for whether to start on the 1st page or 2nd page depending on how far the names from above went
    positions = []
    if count:
        count2 = 0
        startPageLines2 = pdfReader.getPage(2).extractText().split('\n') 
        startLines2 = [line[3:] for line in startPageLines2]
        resultPage2 = ' '.join(startLines2)
        words2 = resultPage2.split(' ')
        for word in words2:
            if (word[:10] == 'Petitioner'):
                positions.append('p')
                count2 += 1
                if(count2 == len(names)):
                    break
            if (word[:10] == 'Respondent'):
                positions.append('r')
                count2 += 1
                if(count2 == len(names)):
                    break
        pageObj = pdfReader.getPage(3)
    else:
        count2 = 0
        startPageLines2 = pdfReader.getPage(1).extractText().split('\n') 
        startLines2 = [line[3:] for line in startPageLines2]
        resultPage2 = ' '.join(startLines2)
        words2 = resultPage2.split(' ')
        for word in words2:
            if (word[:10] == 'Petitioner'):
                positions.append('p')
                count2 += 1
                if(count2 == len(names)):
                    break
            if (word[:10] == 'Respondent'):
                positions.append('r')
                count2 += 1
                if(count2 == len(names)):
                    break
        pageObj = pdfReader.getPage(2)
        pageObj.mergePage(pdfReader.getPage(3))

    # add all the pages as one big string
    for i in range(4, pdfReader.getNumPages()):
        # get each additional page
        pageObj2 = pdfReader.getPage(i)
        pageObj.mergePage(pageObj2)

    # get entire page as one big string
    page1 = pageObj.extractText()

    # split into lines and trim of first characters which are just line numbers
    pageLines = page1.split('\n')
    pageLines2 = [line[3:] for line in pageLines]
    # print(' '.join(pageLines2))

    # get all letter characters and spaces, remove the ret
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

    # the totalNameWords corresponds to each speaker, so we now map these back to what position they were, petitioner or respondent
    # then you aggregate all the words spoken by petitioner and spoken by respondent
    finalWords = [year, pdf_id, "", ""]
    for pos in range(len(positions)):
        if positions[pos] == 'p':
            finalWords[2] = finalWords[2] + " " + totalNameWords[i]
        elif positions[pos] == 'r':
            finalWords[3] = finalWords[3] + " " + totalNameWords[i]
    
    transcripts = transcripts.append(pd.Series(finalWords, index = transcripts.columns), ignore_index=True)
    return transcripts

transcripts = read_pdf('2000', '00-24', transcripts)
transcripts.to_csv('transcripts.csv')
print(datetime.datetime.now() - now)