def basic_decode(key, message, indicator):

    '''
    Function takes a key containing a list of letters to swap
    and a string.
    
    If the indicator is 'e' then the string will be encoded
    If the indicator is 'd' then the string will be decoded

    Returns: The new string
    '''
   
    message = list(message)

    key = key.lower() + key.upper()

    if indicator == "d":
        #reverse string for encoding
        key = key[::-1]

    #loop through each character of the message
    for j in range(len(message)):
        i = 0
        #loop through each potential key change
        while i < len(key):
              if message[j] == key[i]:
                   if i%2 == 0:
                        message[j] = key[i + 1]
                        i += 2
                   else:
                        message[j] = key[i - 1]
                        i += 1
                   continue
              i += 1

    return "".join(message)

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

def get_successors(message, letters):

    '''
    Function takes a message a series of valid letters that
    can be swapped. 

    Returns a list of the successors
    AND
    Returns a string containing the different swaps
    '''
    letters = list(letters)
    letters = sorted(letters)
    potential = []

    
    #get a list of valid pairs
    lst_pairs = []
    for i in range(len(letters) - 1):
        for j in range(i, len(letters)):
            if check_letters(message, letters, i, j):
                lst_pairs.append(letters[i] + letters[j])
    
    
    #add each valid pairing string 
    for pair in lst_pairs:
        potential.append((basic_decode(pair, message, "d"), pair))
    
    # num_pairs = len(potential)
    # output = ""
    # for i in range(len(potential)):
    #     output += f"\n{potential[i]}"
    #     if i != len(potential) - 1:
    #         output += "\n"

    return potential

def is_valid(msg, dictionary_list, threshold):
    
    '''
    Function determines if a string contains valid words
    based on a list of words (dictionary list).

    If the number of words is above the threshold percentage
    then the function returns true otherwise it returns false.
    '''

    # initializing punctuations string
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    # Removing punctuations in string
    for i in msg:
        if i in punc:
            msg = msg.replace(i, "")

    msg = msg.split() 

    #print(msg)

    #count the valid words
    count = 0
    for i in msg:
        if i.lower() in dictionary_list:
            count += 1
    
    #calculate percent
    perc = (count/len(msg))*100
    
    if perc + 0.005 > threshold:
        result = True
    else:
        result = False

    return result


def create_output_string(solution, solved_depth, key, expanded_count, maxfringesize, maxdepth, expandedlist, debug):
    #Creating the output string
    output_string = f"{solution}\n\n"

    if solution != "No solution found.":
        output_string += f"Key: {key}\n"
        output_string += f"Path Cost: {solved_depth}\n\n"
        pass



    output_string += f"Num nodes expanded: {expanded_count}\n"
    output_string += f"Max fringe size: {maxfringesize}\n"
    output_string += f"Max depth: {maxdepth}"

    #Adding the first 10 expanded nodes
    if debug == "y":
        output_string += "\n\n"
        output_string += "First few expanded states:\n"
        for i in range(len(expandedlist)):
            output_string += expandedlist[i]
            if i != len(expandedlist) - 1:
                output_string += "\n\n"
    
    return output_string


def reverse_key(key):
    out = ""
    string1 = key[::-1]
    i = 0
    while i < len(string1):
        out += string1[i + 1]
        out += string1[i]
        i += 2
    return out

