from functions import get_successors
from functions import is_valid
from functions import create_output_string
from functions import reverse_key

# Depth first search
def DFS(startnode, letters, dictionary_list, threshold, debug):

    maxdepth = 0
    key = ""
    prev = None
    currentnode = (startnode, maxdepth, key, prev)
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
        #Add children nodes to the front of the list
        fringelist = [ (i[0], currentnode[1] + 1, i[1], currentnode) for i in successors] + fringelist

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

  
# Iterative deepening depth first search
def IDS(startnode, letters, dictionary_list, threshold, debug):

    

    maxdepth = 0 
    key = ""
    prev = None
    currentnode = (startnode, maxdepth, key, prev)
    fringelist = []
    expandedlist = []

    solution = ""

    expanded_count = 0
    maxfringesize = 1
    solved_depth = 0

    current_depth = 0
    flag = 0
    nodelimit = 1000

    while expanded_count <= nodelimit:
        if current_depth > nodelimit:
            break

        if flag == 0:
            flag = 1
            expandedlist.append(startnode)
            expanded_count += 1

        #increment depth
        if currentnode[1] > maxdepth:
            maxdepth = currentnode[1]

        #Get the children nodes
        successors = get_successors(currentnode[0], letters)

        #
        if currentnode[1] + 1 <= current_depth:
            #Add children nodes to the front of the list
            fringelist = [ (i[0], currentnode[1] + 1, i[1], currentnode) for i in successors] + fringelist
        
        #test if there are no more valid children 
        if len(fringelist) == 0:
            current_depth += 1
            currentnode = (startnode, 0, "", None)
            expandedlist.append(startnode)
            expanded_count += 1
            continue

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
            
            while currentnode[3] != None:
                key += currentnode[2]
                currentnode = currentnode[3]

            break
        
        
            
    
    if len(solution) == 0:
        solution = "No solution found."


    out = create_output_string(solution, solved_depth, reverse_key(key), expanded_count, maxfringesize, maxdepth, expandedlist, debug)
    return out
  
# Breadth first search
def BFS(startnode, letters, dictionary_list, threshold, debug):


    maxdepth = 0
    key = ""
    prev = None
    currentnode = (startnode, maxdepth, key, prev)
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
        #Add children nodes to the front of the list
        fringelist = fringelist + [ (i[0], currentnode[1] + 1, i[1], currentnode) for i in successors]

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
