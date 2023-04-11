import csv
import numpy as np

# KNN classifier
def classify_nn(training_filename, testing_filename, k):

    # Store the classifications of tests
    classification = []

    # Open the data and store in an array
    f_train = open(training_filename, 'r')
    f_test = open(testing_filename, 'r')
    training_data = list(csv.reader(f_train))
    testing_data = list(csv.reader(f_test))
    f_train.close()
    f_test.close()

    # Create a list containing only the classes of the training data;
    # to be zipped with the euclidean distance and ordered for the nearest neighbours
    class_list = [i[len(i)- 1] for i in training_data]
    

    # Classify each test example using the majority class of the k-nearest-neighbours
    # Proximity is calculated according to Euclidian distance
    for r_test in testing_data:
        
        # Compute the Euclidian distance between test data and training data 
        # for each example in the training data.
        euc_dist = []
        for r_train in training_data:
            classless_r_train = r_train[0:(len(r_train) - 1)]
            tmp = np.sqrt(np.sum([np.square(float(r_test[i]) - float(classless_r_train[i])) for i in range(len(r_test))]))
            euc_dist.append(tmp)

        # Find the k-nearest neighbours by sorting the class list according to distance
        dist_class_list = sorted(zip(class_list, euc_dist), key = lambda sortby: sortby[1])
        k_neighbours = dist_class_list[0:k]

        # Perform classificaiton based on the number of yes and no classes
        yes_counts = 0
        no_counts = 0
        yes_counts = np.sum([yes_counts + (i[0] == "yes") for i in k_neighbours])
        no_counts = np.sum([no_counts + (i[0] == "no") for i in k_neighbours])
        if(yes_counts >= no_counts):
            classification.append("yes")
        else:
            classification.append("no")
    
    
    return classification