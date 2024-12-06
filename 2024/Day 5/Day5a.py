import re

numberMappingList = {} # Keeps track of all the ordering rules for each number
middleSum = 0 # Keeps track of middle number sum of all fixed invalid patterns

with open('Day5Input.txt', 'r') as file:
    content = file.readlines() # Reads file line by line
    for line in content: # For each line found in the file
        line = line.strip('\n') # Strip all newline characters found
        if line.strip() == "": # If the line is empty, ignore it
            pass
        else: # If the line is not empty
            orderingRuleCheck = re.search('[0-9][0-9][|][0-9][0-9]', line) # Checks to see if the line contains the syntax ##|##
            # Ordering Rules Parsing
            if orderingRuleCheck is not None: # If line equals ##|##
                parsedNumbers = line.split("|") # Splits the first and second number and adds each entry separately to a list
                if parsedNumbers[0] in numberMappingList: # If a key/value pair was already made for the first number
                    numberMappingList[parsedNumbers[0]].append(parsedNumbers[1]) # Add the second number to the key's value list
                else: # If a key/value pair was not already made for the first number
                    numberMappingList[parsedNumbers[0]] = [parsedNumbers[1]] # Create a key/value pair with the first number as the key and the second number (in a list) as a value
            else: # If the line is a pattern
                parsedPattern = line.split(',') # Splits all the numbers in the pattern
                valid = 1
                x = 0
                for item in parsedPattern: # Looping through pattern
                    for y in range(x+1, len(parsedPattern)): # Checking if any numbers after the current number are in the ordering rules
                        if parsedPattern[y] not in numberMappingList[item]: # If the second number is not in the ordering rule for the primary number
                            valid = 0 # Mark pattern as invalid
                            break
                    x += 1

                if valid == 1: # If the pattern is valid
                    middleSum += int(parsedPattern[len(parsedPattern)//2]) # Add middle number to total sum
    print("Sum of Middle Numbers: ", middleSum) # Prints sum of all the valid pattern's middle numbers
    

