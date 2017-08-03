#  File: Nim.py

#  Description: program to see winner and loser in game of Nim

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 02/01/2016

#  Date Last Modified: 02/02/2016

def main():
    # read file
    in_file = open("nim.txt", 'r')

    # read num of data sets n you will have
    n = in_file.readline()
    n = int(n)
    # while there are enough data sets
    for i in range(0, n):
        # calculate nim sum of line
        line = in_file.readline()
        line = line.strip()
        line = line.split(" ")
        num_line = [int(i) for i in line]

        len_line = len(num_line)
        x = num_line[0]

        # calculate nim-sum X with all heaps
        for i in range(1, len_line):
            x = x^num_line[i]
        # lose game if first nim-sum is zero
        if (x == 0):
            print("Lose Game")
        else:
            # calculate nim-sum with each individual heap
            q = 0
            for i in range(0, len_line):
                p = num_line[i]^x
                # find first heap where individual nim-sum smaller than heap size
                if (p < num_line[i]):
                    counter = num_line[i] - p
                    print("Remove %d counters from Heap %d" %(counter, i+1))
                    break


main()
