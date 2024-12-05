matrix = [] # A list of lists that is used to construct the matrix
rowCount = 0 # Keeps track of the number of rows in the matrix
colCount = 0 # Keeps track of the number of columns in the matrix
totalMatches = 0
horCount = 0
backHorCount = 0
verCount = 0
backVerCount = 0
bottomLeftCount = 0
bottomRightCount = 0
topLeftCount = 0
topRightCount = 0

# Checks for XMAS in word search
def horizontalCheck(row, col):
    global horCount
    match = 0
    if(col < colCount-3): # If X is not found in the 3 rightmost columns
        if(matrix[row][col+1] == 'M' and matrix[row][col+2] == 'A' and matrix[row][col+3] == 'S' ):
            match = 1
            horCount += 1
    return match

# Checks for SAMX in word search
def backwardsHorizontalCheck(row, col):
    global backHorCount
    match = 0
    if(col > 2): # If X is not found in the 3 leftmost columns
        if(matrix[row][col-1] == 'M' and matrix[row][col-2] == 'A' and matrix[row][col-3] == 'S' ):
            match = 1
            backHorCount += 1
    return match

# Checks for vertical XMAS matches in word search
def verticalCheck(row, col):
    global verCount
    match = 0
    if(row < rowCount-3): # If X is not found in the 3 bottom rows
        if(matrix[row+1][col] == 'M' and matrix[row+2][col] == 'A' and matrix[row+3][col] == 'S' ):
            match = 1
            verCount += 1
    return match 

# Checks for backwards vertical matches in word search
def backwardsVerticalCheck(row, col):
    global backVerCount
    match = 0
    if(row > 2): # If X is not found in the top 3 rows
        if(matrix[row-1][col] == 'M' and matrix[row-2][col] == 'A' and matrix[row-3][col] == 'S' ):
            match = 1
            backVerCount += 1
    return match 

# Checks for bottom right and top right matches in word search
def diagonalCheck(row, col):
    global bottomRightCount, topRightCount
    match = 0
    
    # Bottom Right Direction Match
    if(row < rowCount-3 and col < colCount-3): # If X is not found in the bottom 3 rows or 3 rightmost columns
        if(matrix[row+1][col+1] == 'M' and matrix[row+2][col+2] == 'A' and matrix[row+3][col+3] == 'S' ):
            match += 1
            bottomRightCount += 1

    # Top Right direction Match
    if(row > 2 and col < colCount-3): # If X is not found in the top 3 rows or 3 rightmost columns
        if(matrix[row-1][col+1] == 'M' and matrix[row-2][col+2] == 'A' and matrix[row-3][col+3] == 'S' ):
            match += 1
            topRightCount += 1
    return match 

# Checks for top left and bottom left matches in word search
def backwardsDiagonalCheck(row, col):
    global topLeftCount, bottomLeftCount
    match = 0

    # Top Left Direction Match
    if(row > 2 and col > 2): # If X is not found in the top 3 rows or 3 leftmost columns
        if(matrix[row-1][col-1] == 'M' and matrix[row-2][col-2] == 'A' and matrix[row-3][col-3] == 'S' ):
            match += 1
            topLeftCount += 1

    # Bottom Left Direction Match
    if(row < rowCount-3 and col > 2): # If X is not found in the bottom 3 rows or 3 leftmost columns
        if(matrix[row+1][col-1] == 'M' and matrix[row+2][col-2] == 'A' and matrix[row+3][col-3] == 'S' ):
            match += 1
            bottomLeftCount += 1
    return match 

with open('Day4Input.txt', 'r') as file:
    rows = file.readlines() # Reads file line by line
    # Constructs the matrix and sets the row and column counts accordingly
    for row in rows:
        charList = []
        rowCount += 1
        colCount = 0
        for char in row:
            colCount += 1
            charList.append(char)
        matrix.append(charList)

  
for row in range(rowCount): # For each row found in the matrix
    for col in range(colCount): # For each column found in the matrix
        if matrix[row][col] == 'X': # If the current letter is an X in the 2D matrix
            totalMatches += horizontalCheck(row, col)
            totalMatches += backwardsHorizontalCheck(row, col)
            totalMatches += verticalCheck(row, col)
            totalMatches += backwardsVerticalCheck(row, col)
            totalMatches += diagonalCheck(row, col)
            totalMatches += backwardsDiagonalCheck(row, col)

print("Total Matches: " + str(totalMatches))      
print("Horizontal Matches: " + str(horCount))  
print("Backwards Horizontal Matches: " + str(backHorCount))  
print("Vertical Matches: " + str(verCount))  
print("Backwards Vertical Matches: " + str(backVerCount))  
print("Bottom Left Matches: " + str(bottomLeftCount))  
print("Bottom Right Matches: " + str(bottomRightCount))   
print("Top Left Matches: " + str(topLeftCount))  
print("Top Right Matches: " + str(topRightCount))   
