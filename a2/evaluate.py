'''
Evaluates KNN and Naive Bayes classifiers using 10-fold stratified cross-validation.
'''

from classifiers import *
from generate_folds import separate_yes_no
import csv

# Global variables for now because I cbf and it's not marked.
train_filename = 'data/tmp_train.csv'
test_filename = 'data/tmp_test.csv'

def create_files(data_filename, num_folds, test_fold):
    '''
    Separates a large dataset into training and test files for cross-validation.
    Takes as input an integer for the current test fold (1 to 10).
    The remaining folds are training folds.
    Basically a rewrite of get_folds but saves the data into seperate training and
    test files. (Thanks Daniel)    
    '''

    #get training and test data
    f_train = open(data_filename, 'r')
    training_data = f_train.readlines()

    f_train.close()

    #separate data into yes and no classes
    class_separation = separate_yes_no(training_data)
    num_yes = len(class_separation['yes']) - 1
    num_no = len(class_separation['no']) - 1

    #create a list of folds
    fold_list = []
    for i in range(num_folds):
        fold_list.append([])

    #assign yes instances to each fold one by one
    count = 0
    while num_yes >= 0:
        fold = count%num_folds
        fold_list[fold].append(class_separation['yes'][num_yes])
        num_yes -= 1
        count += 1
    
    #assign no instances to each fold one by one
    count = 0
    while num_no >= 0:
        fold = count%num_folds
        fold_list[fold].append(class_separation['no'][num_no])
        num_no -= 1
        count += 1


    #write to the output files
    f_train_folds = open(train_filename, 'w')
    f_test_folds = open(test_filename, 'w')
    fold_count = 1
    for fold in fold_list:
        for instance in fold:
            if(fold_count == test_fold):
                f_test_folds.write(instance)
                f_test_folds.write('\n')
            else:
                f_train_folds.write(instance)
                f_train_folds.write('\n')
                
        fold_count += 1

    return

# Check if create_files is working as intended
# if __name__ == '__main__':
#     create_files('data/pima.csv', 10, 1)

def evaluate(data_filename, algorithm, k = 1):
    '''
    Evaluates algorithms the algorithms under 10-fold stratified cross-validation.
    Currently available algorithms:
        K-Nearest Neighbours (algorithm = 'KNN')
        Naive Bayes (algorithm = 'NB')
    Returns accuracy as a percentage.
    '''
    accuracy_vector = []
    # train_data = []
    # test_data = []
    # selection_list = list(range(10))

    # train_folds = selection_list.copy()
    # test_fold = train_folds.pop()

    # train_data = [train_data + full_data[start_intervals[n]:end_intervals[n]] for n in train_folds]
    # test_data = full_data[start_intervals[test_fold]:end_intervals[test_fold]]
    
    # Separate the classes of the test data from the data itself
    test_classes = [i[len(i)- 1] for i in test_data]
    test_data = [i[0:len(i) - 1] for i in test_data]

    # if(algorithm == 'KNN'):
    #     class_prediction = classify_nn(train_filename, test_filename, k)

    # if(algorithm == 'NB'):
    #     class_prediction = classify_nb(train_data, test_data)

    if(len(accuracy_vector) != 0):
        accuracy = sum(accuracy_vector)/len(accuracy_vector)
    else:
        accuracy = 0

    return accuracy


if __name__ == '__main__':
    # Evaluate the classifiers
    data_file_raw = 'data/pima.csv'
    data_file_CFS = 'data/pima_CFS_no_headers.csv'
    print("Evaluating 1NN Classifier:")
    print("Raw data accuracy = " + str(evaluate(data_file_raw, 1, 1)) + "%\n")
    print("CFS data accuracy = " + str(evaluate(data_file_CFS, 1, 1)) + "%\n")

    # print("Evaluating 5NN Classifier:")
    # print("Accuracy = " + str(evaluate(data_file, 1, 5)) + "%\n")

    # print("Evaluating NB Classifier:")
    # print("Accuracy = " + str(evaluate(data_file, 2)) + "%\n")
