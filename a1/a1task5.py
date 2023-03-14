import math

# Key function for sorting tuples (I call them structs).
# Sorts the struct by the second piece of data (frequency)
def second(n):
    return n[1]
  
# Task 5 develops a hueristic function based on frequency analysis
def task5(message_filename, is_goal):
    # Check if we're at a goal node (hueristic = 0)
    if is_goal:
        return 0
    
    # Open the message
    f = open(message_filename, 'r')
    msg = f.read()
    f.close()
    
    # Determine the frequency of desired letters in the message
    # Note that punctuation doesn't matter so make all letters uppercase (to match freq)
    letters = "AENOST"
    letters = list(letters)
    msg = msg.upper()
    freq = [msg.count(letters[i]) for i in range(len(letters))]
    
    # Store the frequencies alongside the letters in a struct and order based on frequency
    # POSSIBLE ERROR - does this account for alphabetical ordering in the case of a tie?
    letterFreq = [(letters[i], freq[i]) for i in range(len(letters))]
    letterFreq = sorted(letterFreq, key = second, reverse = True)
 
    # Compare the ordering with the goal (ETAONS)
    count = 0
    goal = list("ETAONS")
    for i in range(len(goal)):
        if goal[i] != letterFreq[i][0]:
            count += 1
        
        # print(f"{goal[i]} {letterFreq[i][0]}") # DEBUGGING
    
    return math.ceil(count/2)

if __name__ == '__main__':
  # Example function calls below, you can add your own to test the task5 function
  print(task5('freq_eg1.txt', False))
  print(task5('freq_eg1.txt', True))
  print(task5('freq_eg2.txt', False))
  print(task5('freq_eg3.txt', False))
