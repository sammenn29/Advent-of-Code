import re

total = 0
with open('Day3Input.txt', 'r') as file:
    contents = file.read() # Reads all of the file
    mulList = re.findall("mul[(][0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?[)]", contents) # Finds all mul(#,#) expressions and puts each entry in a list
    for item in mulList: # For all mul(#,#) expressions found
        subitem = item[4:-1] # creates a substring of the two numbers in the mul() statement. The substring includes the comma.
        numberarray = subitem.split(",") # Creates an array with each number being a spot in the array. The array will be used as reference for multiplication.
        total += (int(numberarray[0]) * int(numberarray[1])) # Multiplies the first number by the second number and adds it to the total sum
print("Sum of Results: " + str(total)) # Prints the final number after all mul() have been multiplied and added together