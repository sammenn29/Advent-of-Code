import re

numberMappingList = {}
middleSum = 0

with open('Day5Input.txt', 'r') as file:
    content = file.readlines() # Reads file line by line
    for line in content:
        line = line.strip('\n')
        if line.strip() == "":
            pass
        else:
            orderingRuleCheck = re.search('[0-9][0-9][|][0-9][0-9]', line)
            # Ordering Rules Parsing
            if orderingRuleCheck is not None:
                parsedNumbers = line.split("|")
                if parsedNumbers[0] == '':
                    pass
                elif parsedNumbers[0] in numberMappingList:
                    numberMappingList[parsedNumbers[0]].append(parsedNumbers[1])
                else:
                    numberMappingList[parsedNumbers[0]] = [parsedNumbers[1]]
            else:
                parsedPattern = line.split(',')
                valid = 1
                x = 0
                for item in parsedPattern: # Looping through pattern
                    for y in range(x+1, len(parsedPattern)): # Checking if any numbers after the current number are in the ordering rules
                        for number in numberMappingList[item]:
                            if parsedPattern[y] not in numberMappingList[item]:
                                valid = 0
                                break
                    x += 1

                if valid == 1:
                    middleSum += int(parsedPattern[len(parsedPattern)//2])
    print("Sum of Middle Numbers: ", middleSum)
    

