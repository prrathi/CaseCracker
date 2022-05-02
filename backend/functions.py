from ast import Str
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import csv

justice_dict = pd.read_csv("justice_dictionary.csv")
justice_names = justice_dict["justice"]
df = pd.read_csv("justice_leanings_final.csv")
df1 = df.values
questionCount = [3, 3, 3, 3, 3, 1, 2]
issueAreas = ["Criminal Procedure", "Civil Rights", "First Amendment", "Due Process", "Privacy", "Attorneys", "Economic Activity"]
# Assumption: There are 18 total questions, with the number of questions per issue area stored in question Count. 

# STEPS ON HOW THIS WORKS
# User data is sent, we take the issue average for the user's responses.



# Updated Function to find Issue Average for each of the updated issue areas from final survey.
# See classify.py for original documentation
def findIssueAvg(responses):
    sumPerArea = []
    # lengthResponse = int(len(responses)/3)
    count = 0
    for i in range(len(questionCount)):
        sum = 0
        for j in range(questionCount[i]):
            sum += responses[count]
            count += 1
        sumPerArea.append(round(sum/questionCount[i], 2))
    return sumPerArea


# Function to compare user averages to each justices
# userAvg is a 1d array with the average user political leaning for each issueArea
# targetJustice is a 1d array with the target Justice's average
# Return type: rounded double for distance. Returns -1 if the justice simply does not have enough
# data per issue Area
def distance(userAvg, targetJustice):
    distance = 0
    count = 0
    for i in range(len(targetJustice)):
        if (not math.isnan(targetJustice[i])):
            count += 1
            distance += (targetJustice[i] - userAvg[i]) * (targetJustice[i] - userAvg[i])
    if (count == 0):
        return -1
    distance = distance/count
    if (count >= 7):
        return round(distance,3)
    return -1

# Function to find the two minimum distance issue areas
def minIssueArea(userAvg, targetJustice):

    # Finding the Minimum Issue Area
    issueAreas = []
    minFirst = (targetJustice[0] - userAvg[0]) * (targetJustice[0] - userAvg[0])
    issueOne = 0
    for i in range(len(targetJustice)):
        if (not math.isnan(targetJustice[i]) and ((targetJustice[i] - userAvg[i]) * (targetJustice[i] - userAvg[i]) < minFirst)):
            minFirst = (targetJustice[i] - userAvg[i]) * (targetJustice[i] - userAvg[i])
            issueOne = i
    

    # Finding the second minimum issue area

    minSecond = (targetJustice[0] - userAvg[0]) * (targetJustice[0] - userAvg[0])
    issueSecond = 0
    if (issueOne == 0):
        minSecond = (targetJustice[1] - userAvg[1]) * (targetJustice[1] - userAvg[1])
        issueSecond = 1
    for i in range(len(targetJustice)):
        if ((not math.isnan(targetJustice[i]) and ((targetJustice[i] - userAvg[i]) * (targetJustice[i] - userAvg[i]) < minSecond) )and i != issueOne):
            minSecond = (targetJustice[i] - userAvg[i]) * (targetJustice[i] - userAvg[i])
            issueSecond = i  
    issueAreas = ["Criminal Procedures", "Civil Rights", "First Amendment", "Due Process", "Privacy", "Attorneys", "Economic Activity"]
    areas = [issueAreas[issueOne], issueAreas[issueSecond]]
    return areas
    

# Function to find the closest justice based on distances 
# Calls distance function
# userAvg is a 1d list with the average user political leaning for each issueArea
# justices is a 2d list with each row corresponding to each justice
# return type: int index representing the ID of the closest justice
def findClosestJustice(userAvg):
    # Getting the distance between user and each justice
    distances = []
    for i in range(len(df1)):
        distances.append(distance(userAvg, df1[i]))


    # Finding the first judge that is closest
    minFirst = distances[0]
    minJudgeFirst = 0
    for i in range(len(distances)):
        if ((distances[i] != -1 and distances[i] < minFirst)):
            minFirst = distances[i]
            minJudgeFirst = i
    # Finding the two closest issue areas for the first judge
    minIssueAreaOne = minIssueArea(userAvg, df1[minJudgeFirst])

    # Second judge
    minSecond = distances[0]
    minJudgeSecond = 0
    if (minJudgeFirst == 0):
        minSecond = distances[1]
        minJudgeSecond = 1
    for i in range(len(distances)):
        if ((distances[i] != -1 and distances[i] < minSecond) and i != minJudgeFirst):
            minSecond = distances[i]
            minJudgeSecond = i
    minIssueAreaTwo = minIssueArea(userAvg, df1[minJudgeSecond])

    # Third Judge
    minThird = distances[0]
    minJudgeThird = 0
    if ((minJudgeFirst == 0 and minJudgeSecond == 1) or (minJudgeSecond == 0 and minJudgeFirst == 1)):
        minJudgeThird = 2
        minThird = distances[1]
    elif (minJudgeFirst == 0 or minJudgeSecond == 0):
        minJudgeThird = 1
        minThird = distances[1]
    
    for i in range(len(distances)):
        if ((distances[i] != -1 and distances[i] < minThird) and i!= minJudgeFirst and i != minJudgeSecond):
            minThird = distances[i]
            minJudgeThird = i
    
    # Formatting output of function
    minIssueAreThree = minIssueArea(userAvg, df1[minJudgeThird])
    judgeOne = [justice_names[minJudgeFirst], minIssueAreaOne[0], minIssueAreaOne[1]]
    judgeTwo = [justice_names[minJudgeSecond], minIssueAreaTwo[0], minIssueAreaTwo[1]]
    judgeThree = [justice_names[minJudgeThird], minIssueAreThree[0], minIssueAreThree[1]]
    leaning = findPoliticalLeaning(userAvg)
    minJudge = [judgeOne, judgeTwo, judgeThree, leaning]
    return minJudge


def findPoliticalLeaning(userAvg):
    sum = 0
    for i in range(len(userAvg)):
        sum += userAvg[i]
    sum /= len(userAvg)
    if (sum < 1.4):
        return ["Liberal"]
    if (sum > 1.6):
        return ["Conservative"]
    return ["Moderate"]


# Example method to use main
def main():
    selfResponses = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    issueAverages = findIssueAvg(selfResponses)
    closestJustice = findClosestJustice(issueAverages)
    print(closestJustice)
    
    
    
if __name__ == "__main__":
    main()

