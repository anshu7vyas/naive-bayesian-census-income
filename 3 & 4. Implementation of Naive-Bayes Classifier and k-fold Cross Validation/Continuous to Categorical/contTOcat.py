'''
Created on Apr 4, 2015

@author: NANSH
'''
##############################################################################################################
#This script will go through the dataset and will convert all the continuous data into the categorical data.
#1.	Ignoring or deleting attributes of no significant impact on the analysis.
#After doing data visualization, it became clear that the attribute FNLWGT and Education-num will have no impact on the analysis that we are doing.
#As education attribute is similar to education-num attribute. Keeping one of the two will help reduce unnecessary data.
#I wrote a python script handle-missing.py which implements two strategies of handling the missing values, namely:
#Removing the missing values:
#	we lose a couple thousand rows.
#Replacing the missing values: 
#	we replace the missing values with the most frequent value of the attribute.

#
#usage: python contTOcat.py [INPUT-FILENAME]
##############################################################################################################


from pandas import read_csv, DataFrame
import pandas as pd
import sys

def loadDataSet(filename):
	df = pd.read_csv(filename)
	return df

# A function to convert all the continuous data into categorical data.
def contTOcat(data_set):

	data_set.columns = ['AGE','WORKCLASS','EDUCATION','MARITAL STATUS','OCCUPATION','RELATIONSHIP','RACE','SEX','CAPITAL-GAIN'\
              ,'CAPITAL-LOSS','HOURS-PER-WEEK','NATIVE-COUNTRY','CLASS']


	age = data_set["AGE"]									#Storing the values of "AGE" attribute
	hoursPW = data_set["HOURS-PER-WEEK"]					#Storing the values of "HOURS-PER-WEEK" attribute
	capital_gain = data_set["CAPITAL-GAIN"]					#Storing the values of "CAPITAL-GAIN" attribute
	capital_loss = data_set["CAPITAL-LOSS"]					#Storing the values of "CAPITAL-LOSS" attribute

	# CONVERTING ALL CATEGORICAL ATTIRUBUTES TO CONTINUOUS AND STORING THEM IN NEW COLUMNS
	data_set["CAT-AGE"] = pd.cut(age, [0, 25, 45, 65, 95], labels = ["Young", "Middle-aged", "Senior", "Old"], right = True , include_lowest = True)
	data_set["CAT-HOURSpW"] =  pd.cut(hoursPW, [0, 25, 40, 60, 100], labels = ["Part-time", "Full-Time", "Over-Time", "Too-Much"], right = True , include_lowest = True)
	data_set["CAT-CAPITAL-GAIN"] = pd.cut(capital_gain, [0, 1, 7298, 99999], labels = ["None", "Low", "High"], right = True , include_lowest = True)
	data_set["CAT_CAPITAL_LOSS"] = pd.cut(capital_loss, [0, 1, 1887, 4356], labels = ["None", "Low", "High"], right = True , include_lowest = True)
	
	data_set = data_set.drop('AGE', 1)
	data_set = data_set.drop('CAPITAL-GAIN', 1)
	data_set = data_set.drop('CAPITAL-LOSS', 1)
	data_set = data_set.drop('HOURS-PER-WEEK', 1)

	#print data_set

	data_set.to_csv('dataset-all-categorical.csv', sep = ",", index = False)

 	#data_set.to_csv('dataset-replaced-missing-all-categorical.csv', sep = ",", index = False)

def main():
	filename = sys.argv[1]				# specify which file to convert
	df = loadDataSet(filename)
	
	contTOcat(df)
	
main()