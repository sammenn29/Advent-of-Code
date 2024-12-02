safeReportCount = 0
with open('Day2Input.txt', 'r') as file:
    contents = file.readlines() # Reads file line by line
    for line in contents: # For each line in the file
        separatedNumbers = line.split(' ') # Creates a string array with all the numbers
        pattern = "Increasing"
        if(int(separatedNumbers[0]) > int(separatedNumbers[1])): # If the second number is smaller than the first number in the report
            pattern = "Decreasing"

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
        if validReport == True: # If the indicator remained true throughout the check
            safeReportCount += 1 # The report is considered safe and the overall count is increased by 1

print("Final Safe Report Count: " + str(safeReportCount)) # Total Number of Safe Reports    

