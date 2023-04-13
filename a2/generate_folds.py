import csv

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
        thing = instance.strip()
        thing = thing.split(',')
        output_dict[thing[-1]].append(instance[0:-1])
    
    return output_dict

def get_folds(training_filename, num_folds):
        #get training and test data
    f_train = open(training_filename, 'r')
    training_data = f_train.readlines()

    f_train.close()

    #separate data into yes and no classes
    class_separation = separate_yes_no(training_data)
    num_yes = len(class_separation['yes']) - 1
    num_no = len(class_separation['no']) - 1
    print(num_yes, num_no)
    fold_list = []
    for i in range(num_folds):
        fold_list.append([])
    
    count = 0
    while num_yes >= 0:
        fold = count%num_folds
        fold_list[fold].append(class_separation['yes'][num_yes])
        num_yes -= 1
        count += 1
    
    count = 0
    while num_no >= 0:
        fold = count%num_folds
        fold_list[fold].append(class_separation['no'][num_no])
        num_no -= 1
        count += 1
    
    c = 0
    for i in fold_list:
        for j in i:
            c += 1

    print(c)

    f = open('pima-folds.csv', 'w')
    fold_count = 1
    for fold in fold_list:
        f.write(f"fold{fold_count}\n")
        for instance in fold:
            f.write(instance)
            f.write('\n')
        f.write('\n')
        fold_count += 1




train_file = 'a2\\data\\pima.csv'
get_folds(train_file, 10)