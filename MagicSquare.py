#  File: MagicSquare.py

#  Description: program to print a magic square

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Partner's Name: Marion Milloy

#  Partner's UT EID: mm69994

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 02/06/2016

#  Date Last Modified: 02/06/2016

# Populate a 2-D list with numbers from 1 to n2
def makeSquare(n):
    squareList = []

    # keep original input as nums
    counter = 1

    for row in range (n):
        squareList.append([])
        for col in range(n):
            squareList[row].append(0)
    # place 1
    squareList[n - 1][n//2] = counter

    # initialize position of subsequent n
    i = n - 1
    j = n // 2

    counter += 1
    while (counter <= n**2):
        if (squareList[(i + 1) % n][(j + 1) % n] == 0):
            squareList[(i + 1) % n][(j + 1) % n] = counter
            i = (i + 1) % n
            j = (j + 1) % n
        else:
            squareList[(i - 1)][j] = counter
            # updating row location (coordinate)
            i = i - 1
        counter += 1

    return squareList

# Print the magic square in a neat format where the numbers
# are right justified
def printSquare(magicSquare):
    print("Here is a %d x %d magic square:" %(magicSquare, magicSquare))
    print()
    MS = makeSquare(magicSquare)

    length = len(MS)

    num_list = []
    for i in range (0, length):
        j = 0
        for j in range (0, length):
            y = str(MS[i][j])
            y = y.rjust(2, ' ')
            print(y + " ", end = "")
            #print(str(MS[i][j]) + " ", end = "")
        print()
    print()


# Check that the 2-D list generated is indeed a magic square
def checkSquare(magicSquare):
    MS = makeSquare(magicSquare)
    # calculate sum of rows
    for i in range (0, len(MS)):
        sum_rows = 0
        for j in range (0, len(MS[i])):
            sum_rows += MS[i][j]

    # calculate sum of cols
    for j in range (0, len(MS[i])):
        sum_cols = 0
        for i in range (0, len(MS)):
            sum_cols += MS[i][j]

    # calculate sum of diagonals (UL to LR)
    sum_lr = 0
    for i in range (len(MS)):
        sum_lr += MS[i][i]

    # calculate sum of diagonals (UR to LL)
    sum_rl = 0
    for i in range (len(MS)):
        sum_rl += MS[i][len(MS) - 1 - i]

    print("Sum of row =", sum_rows)
    print("Sum of column =", sum_cols)
    print("Sum diagonal (UL to LR) =", sum_lr)
    print("Sum diagonal (UR to LL) =", sum_rl)

    print()

def main():
    # Prompt the user to enter an odd number 3 or greater
    num = int(input("Please enter an odd number: "))
    print()

    # Check the user input
    if (num >= 3):
        # if num even
        if (num % 2 == 0):
            # ask for input again
            num = int(input("Please enter an odd number: "))
        else:
            # if both conditions pass
            num =  num
    else:
        # if num less than 3
        num = int(input("Please enter an odd number: "))

    # Create the magic square
    makeSquare(num)

    # Print magic square
    printSquare(num)

    # Verify that it is a magic square
    checkSquare(num)

main()
