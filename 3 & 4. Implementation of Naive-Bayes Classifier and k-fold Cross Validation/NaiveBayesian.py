'''
Created on Apr 4, 2015

@author: NANSH
'''
'''
##########################################################################################################################################
#This is the implemetation of the Naive Bayesian Classifier. It takes input of two files: 
# 1. Dataset with all categorical attributes.
# 2. Dataset with continuous attributes probability calculated by gaussian distribution.
#
#
#Usage: python NaiveBayesian.py
##########################################################################################################################################
'''
import pandas as pd
from pandas import read_csv, DataFrame
import random
import numpy as np

def loadDataTrainSet(filename):
    Traindf = pd.read_csv(filename)
    return Traindf

def loadTestSet(fileTest):
    Testdf = pd.read_csv(fileTest)
    return Testdf

def training(Traindf):
    dfGreater50k = Traindf[Traindf['CLASS'] == " >50K"]               #dividing into 2 data frames for each class label
    dfLessThanEqual50k = Traindf[Traindf['CLASS'] == " <=50K"]
    
    count_Greater50k = len(dfGreater50k)                    #taking count of dataframe 1
    count_LessThanEqual50k = len(dfLessThanEqual50k)        #taking count of dataframe 2

    prob_Greater50k = float(count_Greater50k)/float(len(Traindf))
    prob_LessThanEqual50k = float(count_LessThanEqual50k)/float(len(Traindf))

    classProb = {" >50K": prob_Greater50k, " <=50K": prob_LessThanEqual50k }
    
    dfGreatDict = {}
    dfLessDict = {}
    for onecol in dfGreater50k:
        if onecol != 'CLASS':
            # adding to greater than dict
            greatSeries = dfGreater50k[onecol].value_counts()
            thisDict = greatSeries.to_dict()
            thisDict.update((k, float(v)/float(count_Greater50k)) for k, v in thisDict.items())
            dfGreatDict[onecol] = thisDict

            # adding to less than dict
            lessSeries = dfLessThanEqual50k[onecol].value_counts()
            lessDict = lessSeries.to_dict()
            lessDict.update((k, float(v)/float(count_LessThanEqual50k)) for k, v in lessDict.items())
            dfLessDict[onecol] = lessDict
    likelihood = {}
    likelihood[" >50K"] = dfGreatDict
    likelihood[" <=50K"] = dfLessDict
    
    return likelihood, classProb

def testing(likelihood, classProb, Testdf):
    

    myPos = {}
    true = 0
    false = 0
    total = 0

    for record in Testdf.iterrows():
        total += 1
        post = 1
        for k in likelihood:
            for col in Testdf:
                if col != "CLASS":
                    value = record[1][col]
                    if value in likelihood[k][col]:
                        post *= likelihood[k][col][value]
            post *= classProb[k]
            myPos[k] = post
        # get the classifier labels
        ##print (">50k value : {}".format(myPos[" >50K"]))
        ##print (">50k value : {}".format(myPos[" <=50K"]))

        if myPos[" >50K"] > myPos[" <=50K"]:
            max_label = " >50K"
        else:
            max_label = " <=50K"

        trueLabel = record[1]['CLASS']

        # print ("mylabel :{} | true label: {}".format(max_label,trueLabel))   
        

        if trueLabel.strip() == max_label.strip():
            false+= 1
        else:
            true+= 1

    print ("no of True Positives: {}".format(true))
    print ("no of False Positives: {}".format(false))
    print ("Total: {}".format(total))

    # print myPos
    #print max_label
    accuracyCalculator = float(true)/float(total)*100
    
    print accuracyCalculator
    return accuracyCalculator

def main():
    filename = 'adult.data-all-categorical.csv'
    fileTest = 'adult.test-all-categorical.csv'
    Traindf = loadDataTrainSet(filename)
    Testdf = loadTestSet(fileTest)
    
    likelihood, classP= training(Traindf)
    testing(likelihood, classP, Testdf)

main()
