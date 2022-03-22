import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import csv


justice_dict = pd.read_csv("/Users/jamesxie/Desktop/course-project-kk-b/data/user_classification/justice_dict.csv")
# Function to find the average leaning for each 
# Each issue area will have 3 questions, stored in a list "responses"
# Return type: list of ints
def findIssueAvg(responses):
    sumPerArea = []
    lengthResponse = int(len(responses)/3)
    for i in range(lengthResponse):
        sum = 0
        for j in range(3):
            sum += responses[(3 * i) + j]
        sumPerArea.append(round(sum/3.0, 2))
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

# Function to find the closest justice based on distances 
# Calls distance function
# userAvg is a 1d list with the average user political leaning for each issueArea
# justices is a 2d list with each row corresponding to each justice
# return type: int index representing the ID of the closest justice
def findClosestJustice(userAvg, justices):
    distances = []
    for i in range(len(justices)):
        distances.append(distance(userAvg, justices[i]))
    
    minimumDistance = distances[0]
    minJudge = 0
    for i in range(len(distances)):
        if (minimumDistance == -1 or (distances[i] != -1 and distances[i] < minimumDistance)):
            minimumDistance = distances[i]
            minJudge = i
    
    return minJudge + 78

# Function to find the closest cluster for each issue area compared to the user input
# centroids is a 2d list where each row is a different issue area
# userAvg is a 1d list
def findClosestCentroid(userAvg, centroids):
    clusters = []
    for i in range(len(centroids)):
        minimum = (centroids[i][0] - userAvg[i]) * (centroids[i][0] - userAvg[i])
        minIndex = 0
        for j in range(len(centroids[i])):
            minNew = (centroids[i][j] - userAvg[i]) * (centroids[i][j] - userAvg[i])
            if (minNew < minimum):
                minimum = minNew
                minIndex = j
        clusters.append(minIndex)
    return clusters

def findJusticeName(justiceID):
    print (justice_dict.head())
    return(justice_dict.iat[justiceID,1])


# Example method to use main
def main():
    # Import Dataframe
    df = pd.read_csv("/Users/jamesxie/Desktop/course-project-kk-b/data/user_classification/justice_leanings.csv")
    
    df.drop(columns=df.columns[0],  
        axis=1, 
        inplace=True)
    selfResponses = [1, 1.5, 2, 1, 1, 1, 2, 2, 2, 1, 1.2, 1.4, 2, 1.5, 1.75, 1.5, 1.25, 1, 1, 1, 1, 2, 2, 2, 1.5, 1.5, 1.5, 1.1, 1.0, 1.2, 1.5, 1.6, 1.7, 2, 2, 2, 1.2, 1.4, 1.6, 1.5, 1, 2]
    issueAverages = findIssueAvg(selfResponses)
    closestJustice = findClosestJustice(issueAverages, df.values)
    print(findJusticeName(closestJustice))
    
    
    
if __name__ == "__main__":
    main()

