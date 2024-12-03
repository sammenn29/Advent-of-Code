def safeCheck(separatedNumbers): # Checks to see if report is safe given a list of values
    for index in range(len(separatedNumbers)- 1): # For each pair of levels found in the report (does not check last number since there is no number to compare it to)
        validReport = True # Indicator used to verify whether a report is safe or not
        currentDifference = int(separatedNumbers[index+1]) - int(separatedNumbers[index]) # Grabs the difference between the two levels being compared 
        if(currentDifference == 0 or abs(currentDifference) > 3): # If the absolute value difference between the two numbers is 0 or more than 3
            validReport = False # The report is considered unsafe
            break
        else: # If the increase/decrease between two numbers is 1-3
            if(pattern == "Decreasing"): # If the report is of a decreasing pattern
                if(currentDifference > -1): # If a positive gain (including 0) is found in a decreasing level report
                    validReport = False # The report is considered unsafe
                    break
            else:
                if(currentDifference < 1): # If a negative gain (including 0) is found in an increasing level report
                    validReport = False # The report is considered unsafe
                    break
    return validReport

safeReportCount = 0
dampenerCount = 0 

with open('Day2Input.txt', 'r') as file:
    contents = file.readlines() # Reads file line by line
    for line in contents: # For each line in the file
        trimmedline = line.strip('\n')
        separatedNumbers = trimmedline.split(' ') # Creates a string array with all the numbers
        positiveGain = 0
        negativeGain = 0
        pattern = ""
        for index in range(len(separatedNumbers)- 1): # For each pair of levels found in the report (does not check last number since there is no number to compare it to)
            currentDifference = int(separatedNumbers[index+1]) - int(separatedNumbers[index]) # Grabs the difference between the two levels being compared
            if(currentDifference > 0): # If the difference between both numbers is positive
                positiveGain += 1
            elif(currentDifference < 0): # If the difference between both numbers is negative
                negativeGain += 1
        
        if positiveGain > negativeGain: # If there were more increases than decreases
            pattern = "Increasing"
        else: # If there were more decreases than increases
            pattern = "Decreasing"

        if safeCheck(separatedNumbers=separatedNumbers) == True: # If the report passed inspection
            safeReportCount += 1 # The report is considered safe and the overall count is increased by 1
        else: # Go through every possible list combination subtracting one number each time
            tempList = separatedNumbers # Creates temp list of main list
            for count in range(len(separatedNumbers)): # For every combination of the current list of numbers
                currentDelete = tempList[count] # Keeps track of what number was deleted for each run through
                del tempList[count] # Deletes the current number
                if safeCheck(separatedNumbers=tempList) == True: # If the report passed the inspection with one level subtracted
                    safeReportCount += 1 # The report is considered safe and the overall count is increased by 1
                    dampenerCount += 1 # The dampener enhancement made this report safe and adds 1 to the dampener total
                    break
                else: # If the report does not pass inspection
                    tempList.insert(count, currentDelete) # Restore the temp array for next round of deletions

print("Final Safe Report Count: " + str(safeReportCount)) # Total Number of Safe Reports    
print("Final Dampener Count: " + str(dampenerCount)) # Total Number of Dampener Safe Reports