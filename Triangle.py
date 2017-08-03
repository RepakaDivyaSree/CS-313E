#  File: Triangle.py

#  Description: create triangles

#  Student Name: Adam Roach

#  Student UT EID: abr875

#  Partner Name: Eun Seo

#  Partner UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 12 April 2015

#  Date Last Modified: 13 April 2015

# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):

  paths = path_finder (grid)

  n = len(grid)

  maximum = 0
  for path in paths:

    path_sum = 0
    for i in range(n):
      x = grid[i][path[i]]
      path_sum += x

    if path_sum > maximum:
      maximum = path_sum

  return maximum

def path_finder(grid):
  n = len(grid)

  paths = [[0]]

  for _ in range(1, n+1):
    new_paths = []
    for path in paths:
      j = path[-1]
      new_path_a = path[:]
      new_path_b = path[:]
      new_path_a.append(j)
      new_path_b.append(j+1)
      new_paths.append(new_path_a)
      new_paths.append(new_path_b)

    paths = new_paths

  return paths 


# returns the greatest path sum using greedy approach
def greedy (grid):
  return grid[0][0] + greedy_helper(grid, 1, 0)

def greedy_helper (grid, i, j):
  if i >= len(grid):
    return 0
  else:
    if grid[i][j] > grid[i][j+1]:
      return grid[i][j] + greedy_helper(grid,i+1,j)
    else:
      return grid[i][j+1] + greedy_helper(grid,i+1,j+1)

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
  return max(rec_helper(grid, 0, 0, 0))

def rec_helper (grid, i, j, sum):
  # base case -- we've reached the bottom of the triangle
  if i >= len(grid):
    return [sum]
  else:
    if i == len(grid) - 1:
      return rec_helper(grid, i + 1, j, sum + grid[i][j])
    else:
      return rec_helper(grid, i + 1, j, sum + grid[i][j]) + rec_helper(grid, i + 1, j + 1, sum + grid[i][j])

# returns the greatest path sum using dynamic programming
def dynamic_prog (grid):
  return dyn_helper (grid, 0, 0)

def dyn_helper (grid, i, j):
  # base case -- we've reached the bottom of the triangle
  if i >= len(grid):
    return 0
  else:
    a = grid[i][j] + dyn_helper (grid, i + 1, j)
    b = grid[i][j] + dyn_helper (grid, i + 1, j + 1)
    return max(a,b)

# reads the file and returns a 2-D list that represents the triangle
def readFile ():
  # read triangular grid from file
  f = open('triangle.txt', 'r')
  triangle = []

  # we don't really need the first line, so throw it out
  _ = f.readline()

  # build our triangle
  for line in f:
    row = line.strip().split()
    row = [int(x) for x in row]
    triangle.append(row)
  # close file
  f.close()

  return triangle 


def main ():

  triangle = readFile()

  # output greatest path from exhaustive search
  print('The greatest path sum through exhaustive search is ' + str(exhaustive_search(triangle)) + '.')

  # output greatest path from greedy approach
  print('The greatest path sum through greedy search is ' + str(greedy(triangle)) + '.')

  # output greatest path from divide-and-conquer approach
  print('The greatest path sum through recursive search is ' + str(rec_search(triangle)) + '.')

  # output greatest path from dynamic programming 
  print('The greatest path sum through dynamic programming is ' + str(dynamic_prog(triangle)) + '.')




main()