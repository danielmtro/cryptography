import csv
import numpy as np
import math

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

# Calculate the Gaussian probability distribution function for x
def calculate_gaussian(x, mean, stdev):
 exponent = math.exp(-((x-mean)**2 / (2 * stdev**2 )))
 return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


def separate_yes_no(training_data):

    '''
    Function returns a dictionary containing a list of instances where
    the class was yes and when the class was no

    Parameters:
    Training_data (list of integers except final entry of list should be 'yes' or 'no')

    Output:
    Dictionary whose keys are 'yes' and 'no' and whose elements are the instances 
    '''

    #initialise dictionary
    output_dict = {"yes": [], "no": []}

    #loop through the training data, and assign instances
    for instance in training_data:
        #convert all data to floats
        lst = instance[0: -1]
        output_dict[instance[-1]].append([float(x) for x in lst])
    
    return output_dict

def summarise_data(dic):
    '''
    Function takes in a dictionary separated by class and 
    returns a dictionary containing the mean and standard deviation
    of each attribute in each class. 
    e.g. For a dataset containing yes/no class and 2 attributes there would be 4 values
    {
    'yes': [(a1_yes, b1_yes), (a2_yes, b2_yes)],
    'no':  [(a1_no, b1_no), (a2_no, b2_no)]
    }

    Paramters:
    dic: dictionary in the format of the output of separate_yes_no()

    Returns:
    A list of tuples
    '''
    num_attributes = len(dic['yes'][0])
    lst = []
    output_dict = {'yes': [], 'no': []}
    
    yes_list = dic['yes']
    no_list = dic['no']

    stdlist = np.std(yes_list, axis = 0)
    meanlist = np.mean(yes_list, axis = 0)
    for i in range(len(meanlist)):
        lst.append((meanlist[i], stdlist[i]))
    output_dict['yes'] += lst

    lst = []
    stdlist = np.std(no_list, axis = 0)
    meanlist = np.mean(no_list, axis = 0)
    for i in range(len(meanlist)):
        lst.append((meanlist[i], stdlist[i]))
    output_dict['no'] += lst
    
    return output_dict

def predict(summarised_data, instance, yes_probability, no_probability):
    '''
    Function takes in a dictionary containing the statistical information regarding
    each attribute in each class of the training set. Also takes in an instance in the
    form of a list.

    Returns:
    A string Yes or No
    '''

    yes_total = 1
    no_total = 1    

    #Calculate the probability of the instance belonging to yes
    attribute = 0                                             
    for (mean, std) in summarised_data['yes']:
        yes_total *= calculate_gaussian(instance[attribute], mean, std)
        attribute += 1
    yes_total *= yes_probability

    #calculating the probability of the instance belonging to no
    attribute = 0                                             
    for (mean, std) in summarised_data['no']:
        no_total *= calculate_gaussian(instance[attribute], mean, std)
        attribute += 1
    no_total *= no_probability

    #print(yes_total, no_total)
    if no_total > yes_total:
        return 'no'
    else:
        return 'yes'

def classify_nb(training_filename, testing_filename):

    #get training and test data
    f_train = open(training_filename, 'r')
    f_test = open(testing_filename, 'r')
    full_training_data = list(csv.reader(f_train))
    
    #switch to the first line to remove the header line in files.
    #training_data = full_training_data[1:] 
    training_data = full_training_data

    testing_data = list(csv.reader(f_test))

    f_train.close()
    f_test.close()

    #separate data into yes and no classes
    class_separation = separate_yes_no(training_data)

    #get the mean and standard deviation of each attribute 
    summarised_data = summarise_data(class_separation)

    total_instances = len(class_separation['no']) + len(class_separation['yes'])
    yes_probability = len(class_separation['yes'])/total_instances
    no_probability = len(class_separation['no'])/total_instances

    #test each instance of the test set 
    output_list = []
    for instance in testing_data:
        output_list.append(predict(summarised_data, [float(x) for x in instance], yes_probability, no_probability))

    #print(output_list)
    return output_list

train_file = 'a2\\data\\pima.csv'
test_file = 'a2\\data\\example_test.csv'
classify_nb(train_file, test_file)


# f = open('failing.txt', 'r')
# f2 = open('example_test2.txt', 'w')
# for line in f:
#     new = line[line.find("[")+1:line.find("]")].replace('\'', '')
#     new = new.replace(' ', '')
#     f2.write(new)
#     f2.write('\n')
# f.close()
# f2.close()

# f = open(train_file)
# f2 = open('basictraining.csv', 'w')
# count = 0
# for lines in f:
#     line = lines
#     line = line.split(",")
    
#     line = [float(x) if not x.strip().isalpha() else x for x in line ]
#     line = [f"{x:.1f}" if type(x) != str else x for x in line]
#     f2.write(','.join(line))
#     count += 1
#     if count == 5:
#         break
# f.close()
# f2.close()

