leftList = []
rightList = []
with open('Day1aInput.txt', 'r') as file:
    contents = file.readlines() # Reads file line by line
    for line in contents: # For each line in the file
        trimmedLine = line.strip('\n')
        splitline = trimmedLine.split('   ') # Creates a 2 number array that splits the line based on a tab delimiter
        leftList.append(splitline[0]) # First number gets appended to the left list
        rightList.append(splitline[1]) # Second number gets appended to the right list

    leftList.sort() # Sorts the left list in order
    rightList.sort() # Sorts the right list in order

    differenceSum = 0
    for index in range(len(leftList)): # For each number in the left list
        differenceSum += abs(int(leftList[index])-int(rightList[index])) # Find the absolute value difference between the left list and right list number
        
    print("Total Difference Sum: " + str(differenceSum)) # Total Difference Sum between the two lists