from functions import get_successors
from functions import is_valid
from functions import create_output_string
from functions import reverse_key
from functions import h
from functions import fifth
from algorithms import DFS
from algorithms import IDS
from algorithms import BFS

# Greedy search algorithm
def greedy(startnode, letters, dictionary_list, threshold, debug):

    maxdepth = 0
    h_value = h(startnode, is_valid(startnode, dictionary_list, threshold))
    key = ""
    prev = None
    currentnode = (startnode, maxdepth, key, prev, h_value)
    fringelist = []
    expandedlist = [startnode]

    solution = ""

    expanded_count = 0
    maxfringesize = 1
    solved_depth = 0
    flag = 0

    while expanded_count <= 1000:
        if flag == 0:
            flag = 1
            expanded_count += 1

        #increment depth
        if currentnode[1] > maxdepth:
            maxdepth = currentnode[1]

        #Get the children nodes
        successors = get_successors(currentnode[0], letters)
        #Add children nodes to the end of the list
        fringelist = fringelist + [ (i[0], currentnode[1] + 1, i[1], currentnode, h(i[0], is_valid(i[0], dictionary_list, threshold))) for i in successors]
        
        ####### THIS is where the greedy algorithm is actually applied ######
        # Sort the fringe based on the hueristic (asceding order)
        fringelist = sorted(fringelist, key = fifth)
        
        #test maximum size of the fringe
        if len(fringelist) > maxfringesize:
            maxfringesize = len(fringelist)
        
        #remove first node 
        
        currentnode = fringelist.pop(0)
        if expanded_count == 1000:
            break
        expanded_count += 1
        

        #Add to the expanded list
        if len(expandedlist) < 10:
            expandedlist.append(currentnode[0])

        #test if the current node is correct
        if is_valid(currentnode[0], dictionary_list, threshold):
            solution = f"Solution: {currentnode[0]}"
            solved_depth = currentnode[1]
            
            # Set the max depth equal to the solved depth
            maxdepth = solved_depth
            
            while currentnode[3] != None:
                key += currentnode[2]
                currentnode = currentnode[3]

            break
        
        #test if there are no more valid children 
        if len(fringelist) == 0:
            break
    
    if len(solution) == 0:
        solution = "No solution found."


    out = create_output_string(solution, solved_depth, reverse_key(key), expanded_count, maxfringesize, maxdepth, expandedlist, debug)
    return out

# A* search algorithm
def aStar(startnode, letters, dictionary_list, threshold, debug):

    maxdepth = 0
    g_value = h(startnode, is_valid(startnode, dictionary_list, threshold)) + maxdepth
    key = ""
    prev = None
    currentnode = (startnode, maxdepth, key, prev, g_value)
    fringelist = []
    expandedlist = [startnode]

    solution = ""

    expanded_count = 0
    maxfringesize = 1
    solved_depth = 0
    flag = 0

    while expanded_count <= 1000:
        if flag == 0:
            flag = 1
            expanded_count += 1

        #increment depth
        if currentnode[1] > maxdepth:
            maxdepth = currentnode[1]

        #Get the children nodes
        successors = get_successors(currentnode[0], letters)
        #Add children nodes to the end of the list
        fringelist = fringelist + [ (i[0], currentnode[1] + 1, i[1], currentnode, currentnode[1] + 1 + h(i[0], is_valid(i[0], dictionary_list, threshold))) for i in successors]
        
        ####### THIS is where the A* (and greedy) algorithm is actually applied ######
        # Sort the fringe based on the hueristic (asceding order)
        fringelist = sorted(fringelist, key = fifth)
        
        #test maximum size of the fringe
        if len(fringelist) > maxfringesize:
            maxfringesize = len(fringelist)
        
        #remove first node 
        
        currentnode = fringelist.pop(0)
        if expanded_count == 1000:
            break
        expanded_count += 1
        

        #Add to the expanded list
        if len(expandedlist) < 10:
            expandedlist.append(currentnode[0])

        #test if the current node is correct
        if is_valid(currentnode[0], dictionary_list, threshold):
            solution = f"Solution: {currentnode[0]}"
            solved_depth = currentnode[1]
            
            # Set the max depth equal to the solved depth
            maxdepth = solved_depth
            
            while currentnode[3] != None:
                key += currentnode[2]
                currentnode = currentnode[3]

            break
        
        #test if there are no more valid children 
        if len(fringelist) == 0:
            break
    
    if len(solution) == 0:
        solution = "No solution found."


    out = create_output_string(solution, solved_depth, reverse_key(key), expanded_count, maxfringesize, maxdepth, expandedlist, debug)
    return out  
  
def task6(algorithm, message_filename, dictionary_filename, threshold, letters, debug):
    #Get the input messgae
    f = open(message_filename, 'r')
    msg = f.read()
    f.close()

    #Get the dictionary of words
    #Get a list of words in the dictionary
    f = open(dictionary_filename, 'r')
    worddict = [word.strip().lower() for word in f.readlines()]
    f.close()

    if algorithm == "d":
        return DFS(msg, letters, worddict, threshold, debug)

    if algorithm == "b":
        return BFS(msg, letters, worddict, threshold, debug)
    
    if algorithm == "i":
        return IDS(msg, letters, worddict, threshold, debug)
    
    if algorithm == "u":
        return BFS(msg, letters, worddict, threshold, debug)
    
    if algorithm == "g":
        return greedy(msg, letters, worddict, threshold, debug)
      
    if algorithm == "a":
        return aStar(msg, letters, worddict, threshold, debug)

    return ''

if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task6 function
    # print(task6('g', 'secret_msg.txt', 'common_words.txt', 90, 'AENOST', 'n'))
    print(task6('a', 'secret_msg.txt', 'common_words.txt', 90, 'AENOST', 'n'))
    # print(task6('d', 'cabs_plain.txt', 'common_words.txt', 100, 'ABC', 'y'))
    # print(task6('b', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    # print(task6('i', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    
    