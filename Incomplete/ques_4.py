#!/usr/bin/env python

import sys
import os
import numpy as np

"""Feel free to add any extra classes/functions etc as and when needed.
This code is provided purely as a starting point to give you a fair idea
of how to go about implementing machine learning algorithms in general as
a part of the first assignment. Understand the code well"""


class FeatureVector(object):
	def __init__(self,vocabsize,numdata):
		self.vocabsize = vocabsize
		self.X =  np.zeros((numdata,self.vocabsize), dtype=np.int)
		self.Y =  np.zeros((numdata,), dtype=np.int)

	def make_featurevector(self, input, classid):
		"""
		Takes input the documents and outputs the feature vectors as X and classids as Y.
		"""

class KNN(object):
	def __init__(self,trainVec,testVec):
		self.X_train = trainVec.X
		self.Y_train = trainVec.Y
		self.X_test = testVec.X
		self.Y_test = testVec.Y
		self.metric = Metrics('accuracy')

	def classify(self, nn=1):
		"""
		Takes input X_train, Y_train, X_test and Y_test and displays the accuracies.
		"""


class Metrics(object):
	def __init__(self,metric):
		self.metric = metric

	def score(self):
		if self.metric == 'accuracy':
			return self.accuracy()
		elif self.metric == 'f1':
			return self.f1_score()

	def get_confmatrix(self,y_pred,y_test):
		"""
		Implements a confusion matrix
		"""

	def accuracy(self):
		"""
		Implements the accuracy function
		"""

	def f1_score(self):
		"""
		Implements the f1-score function
		"""

if __name__ == '__main__':
	datadir = '/DUMMY - SHARE/datasets/q4'
	classes = ['galsworthy/','galsworthy_2/','mill/','shelley/','thackerey/','thackerey_2/','wordsmith_prose/','cia/','johnfranklinjameson/','diplomaticcorr/']
	inputdir = ['train/','test/']

	vocab = 30000
	trainsz = 10000
	testsz = #Write code

	print('Making the feature vectors.')
	trainVec = FeatureVector(vocab,trainsz)
	testVec = FeatureVector(vocab,testsz)
	ignore_word = ['<s>' , 'a' , 'an' , 'the' , '<\s>' , 'is' , 'to' , 'of']
	arr={};
	for idir in inputdir:
		for j,c in enumerate(classes):
			classid = j+1;
			listing = os.listdir(datadir+idir+c)
			for filename in listing:
				fh = open(datadir+idir+c+filename,'r')
				for lines in fh:
					lines = lines.strip()
					words = lines.split()
					for i in words:
						if i not in ignore_word:
							arr[i] = arr.get(i,0)+1;

				if idir == 'train/':
					trainVec.make_featurevector(inputs,classid)
				else:
					testVec.make_featurevector(inputs,classid)
			# classid += 1

	print('Finished making features.')
	print('Statistics ->')
	print(trainVec.X.shape,trainVec.Y.shape,testVec.X.shape,testVec.Y.shape)

	knn = KNN(trainVec,testVec)
	knn.classify()
