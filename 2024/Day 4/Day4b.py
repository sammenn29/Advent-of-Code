matrix = []
rowCount = 0
colCount = 0
totalMatches = 0

# Checks for MAS spelled in X formats in the word search
def XCheck(row, col):
    match = 0
    if(row > 0 and col > 0 and row < rowCount-1 and col < colCount-1): # If the A character is not an edge character (NOT row=0,139 OR col=0,139)
        
        #M S
        # A
        #M S
        if(matrix[row-1][col-1] == 'M' and matrix[row+1][col-1] == 'M' and matrix[row-1][col+1] == 'S' and matrix[row+1][col+1] == 'S'):
            match += 1

        #M M
        # A
        #S S
        if(matrix[row-1][col-1] == 'M' and matrix[row+1][col-1] == 'S' and matrix[row-1][col+1] == 'M' and matrix[row+1][col+1] == 'S'):
            match += 1
        
        #S S
        # A
        #M M
        if(matrix[row-1][col-1] == 'S' and matrix[row+1][col-1] == 'M' and matrix[row-1][col+1] == 'S' and matrix[row+1][col+1] == 'M'):
            match += 1

        #S M
        # A
        #S M
        if(matrix[row-1][col-1] == 'S' and matrix[row+1][col-1] == 'S' and matrix[row-1][col+1] == 'M' and matrix[row+1][col+1] == 'M'):
            match += 1


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
        if matrix[row][col] == 'A': # If the current character in the matrix is an A
            totalMatches += XCheck(row, col)
            
print("Total Matches: " + str(totalMatches))      