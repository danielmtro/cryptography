'''
Evaluates KNN and Naive Bayes classifiers using 10-fold stratified cross-validation.
'''

from classifiers import *
from generate_folds import separate_yes_no
import csv
import itertools

# Global variables for now because I cbf and it's not marked.
train_filename = 'data/tmp_train.csv'
test_filename = 'data/tmp_test.csv'
test_class_filename = 'data/tmp_true_test_class.csv'

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
    f_test_class = open(test_class_filename, 'w')
    fold_count = 1
    for fold in fold_list:
        for instance in fold:
            if(fold_count == test_fold):
                # Strip the class from the test data and save in seperate files
                if 'no' in instance:
                    write_test = instance.replace(',no', '')
                    write_class = 'no'
                elif 'yes' in instance:
                    write_test = instance.replace(',yes', '')
                    write_class = 'yes'

                f_test_folds.write(write_test)
                f_test_folds.write('\n')
                f_test_class.write(write_class)
                f_test_class.write('\n')

            else:
                f_train_folds.write(instance)
                f_train_folds.write('\n')
                
        fold_count += 1


    f_train_folds.close()
    f_test_folds.close()
    f_test_class.close()
    return

# # Check if create_files function is working as intended
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

    n_folds = 10

    # Move through and test each fold against the algorithm trained on the other folds
    for i in range(n_folds, 0, -1):

        # run create files for each fold seperation
        create_files(data_filename, n_folds, i)

        # Get the true test classes
        f_test_classes = open(test_class_filename, 'r')
        true_test_classes = list(itertools.chain.from_iterable(list(csv.reader(f_test_classes))))

        f_test_classes.close()

        if(algorithm == 'KNN'):
            class_prediction = classify_nn(train_filename, test_filename, k)
        elif(algorithm == 'NB'):
            class_prediction = classify_nb(train_filename, test_filename)
        else:
            class_prediction = 0

        # Compare the prediction with the true test value
        num_correct = sum([class_prediction[i] == true_test_classes[i] for i in range(len(class_prediction))])
        total_num = len(true_test_classes)
        accuracy_vector.append((num_correct/total_num)*100)
            
    # Average the accuracy of each test
    if(len(accuracy_vector) != 0):
        accuracy = sum(accuracy_vector)/(len(accuracy_vector))
    else:
        accuracy = 0

    return accuracy


if __name__ == '__main__':
    # Evaluate the classifiers
    data_file_raw = 'data/pima.csv'
    data_file_CFS = 'data/pima_CFS_no_header.csv'
    print("Evaluating 1NN Classifier:")
    print("Raw data accuracy = " + str(evaluate(data_file_raw, 'KNN', 1)) + "%\n")
    print("CFS data accuracy = " + str(evaluate(data_file_CFS, 'KNN', 1)) + "%\n")
    
    print("\n----------------------------------\n")

    print("Evaluating 5NN Classifier:")
    print("Raw data accuracy = " + str(evaluate(data_file_raw, 'KNN', 5)) + "%\n")
    print("CFS data accuracy = " + str(evaluate(data_file_CFS, 'KNN', 5)) + "%\n")

    print("\n----------------------------------\n")

    print("Evaluating NB Classifier:")
    print("Raw data accuracy =" + str(evaluate(data_file_raw, 'NB')) + "%\n")
    print("CFS data accuracy = " + str(evaluate(data_file_CFS, 'NB')) + "%\n")
