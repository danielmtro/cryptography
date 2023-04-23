'''
Evaluates KNN and Naive Bayes classifiers using 10-fold stratified cross-validation.
Provide the already stratified with 10 folds of data.
algorithm = 1 for KNN classifier | Input number of neighbours (k) as a 3rd input.
algorithm = 2 for NB classifier
Returns accuracy as a percentage.
'''

from classifiers import *
import csv

def evaluate(strat_fold_data, algorithm, k = 1):
    
    # Open stratified dataset
    data = open(strat_fold_data, 'r')
    full_data = list(csv.reader(data))
    
    # Find the fold intervals in the data file
    start_intervals = []
    end_intervals = []

    for row in full_data:
        for item in row:
            if 'fold' in item:
                start_intervals.append(full_data.index(row) + 1)
                # start_intervals.append(row + 1)

    # The end interval of one fold is the start interval of the other, minus the whitesapce
    # Assumes whitespace after one fold and before the next.
    end_intervals = start_intervals.copy()
    end_intervals.pop(0)
    end_intervals.append(len(full_data) + 1)
    end_intervals = [interval - 2 for interval in end_intervals]

    # print(start_intervals)
    # print(end_intervals)

    # Perform 10-fold cross-validation

    # Need to pass the data through files into the classifiers
    train_filename = 'data/tmp_train.csv'
    test_filename = 'data/tmp_test.csv'

    accuracy_vector = []
    train_data = []
    test_data = []
    selection_list = list(range(10))

    train_folds = selection_list.copy()
    test_fold = train_folds.pop()

    train_data = [train_data + full_data[start_intervals[n]:end_intervals[n]] for n in train_folds]
    test_data = full_data[start_intervals[test_fold]:end_intervals[test_fold]]
    
    # Separate the classes of the test data from the data itself
    test_classes = [i[len(i)- 1] for i in test_data]
    test_data = [i[0:len(i) - 1] for i in test_data]
    # print("training data:")
    # print(train_data)
    # print("testing data:")
    # print(test_data)
    # print("testing classes:")
    # print(test_classes)

    # Write the test and train data to a file (to be passed into the classifiers)
    train_file = open(train_filename, 'w')
    writer = csv.writer(train_file)
    for row in train_data:
        writer.writerow(row)
    train_file.close()

    # test_file = open(test_filename, 'w')
    # writer = csv.writer(train_file)
    # writer.writerows(train_data)

    # train_file.close()
    # test_file.close()

    # if(algorithm == 1):
    #     class_prediction = classify_nn(train_filename, test_filename, k)

    # # Compare the accuracy of the test class with the true value of the test data
    
    # if(algorithm == 2):
    #     class_prediction = classify_nb(train_data, test_data, train_data)





    # print(accuracy_vector)
    # accuracy = sum(accuracy_vector)/len(accuracy_vector)
    accuracy = 0
    return accuracy


if __name__ == '__main__':
    # Evaluate the classifiers
    data_file = 'data/pima-folds.csv'
    print("Evaluating 1NN Classifier:")
    print("Accuracy = " + str(evaluate(data_file, 1, 1)) + "%\n")

    # print("Evaluating 5NN Classifier:")
    # print("Accuracy = " + str(evaluate(data_file, 1, 5)) + "%\n")

    # print("Evaluating NB Classifier:")
    # print("Accuracy = " + str(evaluate(data_file, 2)) + "%\n")
