'''
Created on Apr 4, 2015

@author: NANSH
'''

'''
#########################################################################################################
#We handle the missing values in two ways:
#1. Removing the values completely.
#2. Replacing the values with the most frequent(categorical) and average(continuous).
#
#usage: python handle-missing.py
#########################################################################################################
'''

from pandas import read_csv, DataFrame
import pandas as pd
import sys

#Load the dataset
def loadDataSet(filename):
    df = pd.read_csv(filename)
    return df

#1. Strategy 1 : REPLACING MISSING VALUES WITH THE MOST FREQUENT VALUE IN THE ATTRIBUTE
def replace_missing(data_set):
	data_set['WORKCLASS'] = data_set['WORKCLASS'].replace(to_replace = ' ?', value = ' Private')
	data_set['EDUCATION'] = data_set['EDUCATION'].replace(to_replace = ' ?', value = ' HS-grad')
	data_set['MARITAL STATUS'] = data_set['MARITAL STATUS'].replace(to_replace = ' ?', value = ' Married-civ-spouse')
	data_set['OCCUPATION'] = data_set['OCCUPATION'].replace(to_replace = ' ?', value = ' Prof-specialty')
	data_set['RELATIONSHIP'] = data_set['RELATIONSHIP'].replace(to_replace = ' ?', value = ' Husband')
	data_set['RACE'] = data_set['RACE'].replace(to_replace = ' ?', value = ' White')
	data_set['SEX'] = data_set['SEX'].replace(to_replace = ' ?', value = ' Male')
	data_set['NATIVE-COUNTRY'] = data_set['NATIVE-COUNTRY'].replace(to_replace = ' ?', value = ' United-States')

	data_set = data_set.to_csv('DATA-replaced-missing.csv', sep =',', index = False)	#Output file 1
	return data_set

#2. Strategy 2 : REMOVING MISSING VALUES FROM THE DATASET. HERE WE LOSE A COUPLE THOUSAND ROWS
def remove_missing(data_set):
	
	data_set = data_set[data_set['WORKCLASS'] != ' ?']
	data_set = data_set[data_set['EDUCATION'] != ' ?']
	data_set = data_set[data_set['MARITAL STATUS'] != ' ?']
	data_set = data_set[data_set['OCCUPATION'] != ' ?']
	data_set = data_set[data_set['RELATIONSHIP'] != ' ?']
	data_set = data_set[data_set['RACE'] != ' ?']
	data_set = data_set[data_set['SEX'] != ' ?']
	data_set = data_set[data_set['NATIVE-COUNTRY'] != ' ?']
	
	data_set = data_set.to_csv('DATA-removed-missing.csv', sep = ',', index = False)	#Output file 2
	return data_set

def main():
	filename = sys.argv[1]
	df = loadDataSet(filename)
	
	df.columns = ['AGE','WORKCLASS','FNLWGT','EDUCATION','EDUCATION-NUM','MARITAL STATUS','OCCUPATION','RELATIONSHIP','RACE','SEX','CAPITAL-GAIN'\
             ,'CAPITAL-LOSS','HOURS-PER-WEEK','NATIVE-COUNTRY','CLASS']

	# DATA-PREPROCESSING - REMOVING THE COLUMNS FNLWGT AND EDUCATION-NUM
	df = df.drop('FNLWGT', 1)			
	df = df.drop('EDUCATION-NUM', 1)

	#print df[:35]
	remove_missing(df)
	replace_missing(df)
	

main()
