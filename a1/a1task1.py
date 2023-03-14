def basic_code(key, filename, indicator):
    f = open(filename, 'r')
    message = []

    #loop through input file to get the string
    while True:
        char = f.read(1)
        if not char:
                f.close()
                break
        message.append(char)
        
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
             
            
if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task1 function
    print(basic_code('AE', 'spain.txt', 'd'))
    print(basic_code('VFSC', 'ai.txt', 'd'))
    print(basic_code('ABBC', 'cabs_plain.txt', 'e'))