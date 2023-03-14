
def task3(message_filename, dictionary_filename, threshold):
    
    #Get a list of words in the dictionary
    f = open(dictionary_filename, 'r')
    words = [word.strip().lower() for word in f.readlines()]
    f.close()
    
    #print(words)

    #Get a list of words in the original message
    f = open(message_filename, 'r')
    msg = f.read()

    # initializing punctuations string
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    # Removing punctuations in string
    for i in msg:
        if i in punc:
            msg = msg.replace(i, "")

    msg = msg.split() 
    f.close()

    #print(msg)

    #count the valid words
    count = 0
    for i in msg:
        if i.lower() in words:
            count += 1
    
    #calculate percent
    perc = (count/len(msg))*100
    
    if perc + 0.005 > threshold:
        result = True
    else:
        result = False

    return f"{result}\n{perc:.2f}"


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task3 function
    print(task3('jingle_bells.txt', 'dict_xmas.txt', 90))
    print(task3('fruit_ode.txt', 'dict_fruit.txt', 80))
    