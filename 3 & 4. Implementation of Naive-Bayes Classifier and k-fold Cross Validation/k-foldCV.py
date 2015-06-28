'''
Created on Apr 4, 2015

@author: NANSH
'''
'''
###################################################################################################
#We implement the k-fold validatation on our NaiveBayesian classifier.
#Here we have implemented k = 10.
#
#USAGE: python k-foldCV.py
#You just have to change the input, and the input files are provided in the folder with the script
###################################################################################################
'''
import pandas as pd
from pandas import read_csv, DataFrame
import random
import numpy as np
from NaiveBayesian import *
#from 

def loadDataSet(filename):
	data_set = pd.read_csv(filename)
	return data_set

def kFoldCV(df, k=10):
	print len(df)
	chunkSize = int(len(df))/k
	print chunkSize

	chunkDf = {}  # dictionary of df 
	startLoc = -1
	endLoc = chunkSize
	for i in range(k):
		chunkDf[i]= [startLoc + 1, endLoc]
		startLoc += chunkSize
		endLoc += chunkSize
	return chunkDf

def testClassifier(chunkDf, df):
	accuracyList = []
	for k, v in chunkDf.items():
		test = df[v[0]:v[1]]
		trainingSet = df.drop(df.index[v[0]:v[1]])
		likelihood, classprob = training(trainingSet)
		accuracy = testing(likelihood, classprob, test)
		accuracyList.append(accuracy)
	meanAcuracy = np.mean(accuracyList)
	print ("mean accuracy: {} %".format(meanAcuracy))
	# calculate accuracy avg and return


def main():
	filename = 'dataset-all-categorical.csv'
	df = loadDataSet(filename)


	#print df
	listofchunk = kFoldCV(df, 10)
	print listofchunk
	testClassifier(listofchunk, df)

main()
