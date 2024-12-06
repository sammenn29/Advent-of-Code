import re

numberMappingList = {} # Keeps track of all the ordering rules for each number
invalidPatterns = [] # Keeps track of all patterns that were originally invalid and needed to be fixed
middleSum = 0 # Keeps track of middle number sum of all fixed invalid patterns

# Checks to see if a pattern follows the ordering rules. 
def checkPattern(parsedPattern):
    global numberMappingList
    result = []
    valid = 1
    x = 0
    for item in parsedPattern: # Looping through pattern in text file
        for y in range(x+1, len(parsedPattern)): # Checking if any numbers after the current number are in the ordering rules
            if parsedPattern[y] not in numberMappingList[item]: # If the second number is not in the ordering rule for the primary number
                temp = parsedPattern[y] # Holds in memory what the second number is
                valid = 0
                parsedPattern.remove(temp) # Removes second number from pattern
                parsedPattern.insert(x, temp) # Insers the second number right before the primary number in the pattern
                break
        x += 1
    result.append(valid) # result[0] holds result on whether pattern was valid or not
    result.append(parsedPattern) # result[1] holds original pattern (or modified pattern if not valid)
    return result
    

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
                result = checkPattern(parsedPattern) # Checks to see if the pattern is valid
                if result[0] == 0: # If the pattern is invalid
                    invalidPatterns.append(result[1]) # Add pattern to invalidPattern list

    for pattern in invalidPatterns: # Loop through all invalid patterns
        result = 0
        while result == 0: # While the pattern is invalid
            output = checkPattern(pattern) # Checks to see if patern is valid
            result = output[0]
            if output[0] == 1: # If pattern becomes valid
                middleSum += int(pattern[len(pattern)//2]) # Add middle number to total sum

    print("Sum of Middle Numbers: ", middleSum) # Prints total sum of all the invalid pattern middle numbers