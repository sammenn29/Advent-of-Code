leftList = []
rightList = []
comparisonDict = {}
with open('Day1bInput.txt', 'r') as file:
    contents = file.readlines() # Reads file line by line
    for line in contents: # For each line in the file
        trimmedLine = line.strip('\n')
        splitline = trimmedLine.split('   ') # Creates a 2 number array that splits the line based on a tab delimiter
        leftList.append(splitline[0]) # First number gets appended to the left list
        rightList.append(splitline[1]) # Second number gets appended to the right list

    leftList.sort() # Sorts the left list in order
    rightList.sort() # Sorts the right list in order

    similarityScore = 0
    rightIndex = 0
    for index in range(len(leftList)): # For each number in the left list
        while(int(leftList[index]) > int(rightList[rightIndex])): # If the number in the left list is greater than the current number in the right list
                rightIndex += 1 # Adds 1 to the right index to compare the next number in the right list with the left list number
        if(leftList[index] in comparisonDict): # If the number has already been calculated previously (left list duplicate number)
            similarityScore += int(leftList[index]) * comparisonDict[leftList[index]] # Add the same similarity score as what was previously calculated. Similarity score is stored in python dictionary [comparisonDict]
        else: # If the number has not been previously calculated 
            rightCount = 0 # Resets the counter for right list matches to 0
            while(int(leftList[index]) == int(rightList[rightIndex])): # If the current right list number matches with the current left list number
                rightCount += 1 # Adds 1 to the right list match counter
                rightIndex += 1 # Adds 1 to the right Index to look at the next number in the right List
            comparisonDict[leftList[index]] = rightCount # Adds key/value pair (Key: left list number, Value: count of right list matches) to the comparisonDict dictionary
            similarityScore += int(leftList[index]) * comparisonDict[leftList[index]] # Append the product of the left list number multiplied by the count of right list matches
        
    print("Total Similarity Score: " + str(similarityScore)) # Prints the Total Similarity Score between the Two Lists