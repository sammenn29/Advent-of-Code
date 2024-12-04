import re

total = 0
validList = []
with open('Day3Input.txt', 'r') as file:
    contents = file.read() # Reads all of the file
    # Stage 1: Split the input by all dos
    conditionInput = re.split("do[(][)]", contents) # Splits the file's contents by every do() found
    # Stage 2: Eliminate any content that comes after don't()
    for phrase in conditionInput: # For all do() statements found in the file (includes the beginning of the text as well since do() was turned on by default)
        target = re.search("don't[(][)]", phrase) # Finds whether there is a don't() in the current string
        if target is None: # If there are no don't()s detected in the current string
            validList.append(phrase) # Append the current string as it is
        else: # If there is at least 1 don't() detected in the current string
            validString = phrase[0:target.start()] # Erases all content after (and including) the don't()
            validList.append(validString) # Appends the substring
    # Stage 3: Join all do() sections together into one string and use same logic as the Day 3a solution.
    cleanString = ''.join(validList) # Combines all the substrings that have filtered out the don't() content
    mulList = re.findall("mul[(][0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?[)]", cleanString) # Finds all mul(#,#) expressions and puts each entry in a list
    for item in mulList: # For all mul(#,#) expressions found
        subitem = item[4:-1] # creates a substring of the two numbers in the mul() statement. The substring includes the comma.
        numberarray = subitem.split(",") # Creates an array with each number being a spot in the array. The array will be used as reference for multiplication.
        total += (int(numberarray[0]) * int(numberarray[1])) # Multiplies the first number by the second number and adds it to the total sum
print("Sum of Results: " + str(total)) # Prints the final number after all mul() have been multiplied and added together