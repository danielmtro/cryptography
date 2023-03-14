from a1task1 import basic_code

def check_letters(string, lst_letters, index1, index2):
    ''' 
        Function takes in a list of letters, a string and
        two indexes. Returns False under the following 
        conditions.

        1. The letters are the same
        2. Both letters aren't in the string
    '''
    
    letter1 = lst_letters[index1].lower()
    letter2 = lst_letters[index2].lower()
    
    if letter1 == letter2: 
        return False

    string = string.lower()
    if letter1 not in string and letter2 not in string:
        return False
    
    return True

def task2(filename, letters):

    letters = list(letters)
    letters = sorted(letters)
    potential = []

    message = ""
    #loop through input file to get the string
    f = open(filename, 'r')
    while True:
        char = f.read(1)
        if not char:
                f.close()
                break
        message += char
    
    #get a list of valid pairs
    lst_pairs = []
    for i in range(len(letters) - 1):
        for j in range(i, len(letters)):
            if check_letters(message, letters, i, j):
                lst_pairs.append(letters[i] + letters[j])
    
    
    #add each valid pairing string 
    for pair in lst_pairs:
        potential.append(basic_code(pair, filename, "d"))
    
    num_pairs = len(potential)
    output = f"{num_pairs}"
    for i in range(len(potential)):
        output += f"\n{potential[i]}"
        if i != len(potential) - 1:
            output += "\n"


    return output


print(task2('spain.txt', 'ABE'))