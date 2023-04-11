'''
Main test file for KNN and Naive Bayes classifiers
Created: 11/04/23
'''

from classifiers import *

# Test the classifier on the pima data
output = classify_nn('./data/pima.csv', './data/example_test.csv', 5)
print(output)