
#  File: TestSparseMatrix.py

#  Description: Sparse matrix representation has a single linked 
#  list having the row, column, and non-zero data in each link

#  Student Name: Adam Roach

#  Student UT EID: abr875

#  Partner Name: Eun Seo

#  Partner UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 12 April 2015

#  Date Last Modified: 12 April 2015

class Link (object):
  def __init__ (self, row, col, data, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = None

  def __str__ (self):
    s = ''
    return s

class SparseMatrix (object):
  def __init__ (self, row = 0, col = 0):
    self.num_rows = row		# number of rows
    self.num_cols = col		# number of columns
    self.matrix = None

  # setElement() perform an assignment operation a[i][j] = value
  # if value is 0 the link if it exists is deleted
  # if value is non zero then the current value is updated if a
  # link already exists or a new link is added
  def setElement (self, row, col, data):
    if (data == 0):
      self.deleteLink (row, col)
    else:
      self.insertLink (row, col, data)

  def insertLink (self, row, col, data):
    # do nothing if data = 0
    if (data == 0):
      return

    # create a new link
    newLink = Link (row, col, data)

    # if matrix is empty then the newLink is the first link
    if (self.matrix == None):
      self.matrix = newLink
      return

    # find position to insert
    previous = self.matrix
    current = self.matrix

    while ((current != None) and (current.row < row)):
      previous = current
      current = current.next

    # if the row is missing
    if ((current != None) and (current.row > row)):
      previous.next = newLink
      newLink.next = current
      return
  
    # on the row, search by column
    while ((current != None) and (current.col < col)):
      previous = current
      current = current.next

    # if link already there do not insert but reset data
    if ((current != None) and (current.row == row) and (current.col == col)):
      current.data = data
      return

    # now insert newLink
    previous.next = newLink
    newLink.next = current

  # deletes and returns a Link if it is there or None otherwise
  def deleteLink (self, row, col):
    return

  # return a row of the sparse matrix
  def getRow (self, row_num):
    # create a blank list
    a = []

    # search for the row
    current = self.matrix
    if (current == None):
      return a

    while ((current != None) and (current.row < row_num)):
      current = current.next

    if ((current != None) and (current.row > row_num)):
      for i in range (self.num_cols):
        a.append (0)
      return a

    if ((current != None) and (current.row == row_num)):
      for j in range (self.num_cols):
        if (current.col == j):
          a.append (current.data)
          current = current.next
        else:
          a.append (0)
    return a
        
  # return a column of the sparse matrix
  def getCol (self, col_num):
    # create a blank list 
    a = []

    # the links should be "in order", so go through the links and add every link in the column to the list
    current = self.matrix 
    if current==None:
      return a 

    idx = 0 
    while current != None and idx <= self.num_rows:
      if current.col == col_num:
        if current.row == idx:
          a.append(current.data)
          current = current.next 
        else:
          a.append(0)
        idx += 1
      else:
        current = current.next 

    # if there are zeros left at the end of the column, we need to add them new
    while len(a) < self.num_rows:
      a.append(0)

    return a 

  # this function returns the data at a position in the matrix, or zero if there is no data in that position
  def get_data_at (self, i, j):
    current = self.matrix 
    # navigate to the appropriate row
    while current != None and current.row < i:
      current = current.next 

    # navigate to the appropriate column
    while current != None and current.col < j:
      current = current.next 

    # now we are either at (i,j), or past it
    if current == None:
      return 0
    
    if current.row == i and current.col == j:
      return current.data 
    else: # i.e., current.col > j
      return 0  


  # add two sparse matrix
  def __add__ (self, other):
    # assume that the matrices are the same size
    # set number of rows and columns to cycle through
    m = self.num_rows
    n = self.num_cols

    # create a new matrix that's the sum of self and other 
    sum_matrix = SparseMatrix(m,n)

    # cycle through the rows and columns and sum the elements of self and other;
    # add them to the list if they are non-zero
    for i in range(m):
      for j in range(n):
        el = self.get_data_at(i,j) + other.get_data_at(i,j)
        sum_matrix.insertLink(i,j,el)
        el = 0

    return sum_matrix

  # multiply two sparse matrices
  def __mul__ (self, other):
    # get some key dimensions
    m = self.num_rows
    n = self.num_cols
    r = other.num_cols
    
    # make a new matrix to store the product
    product_matrix = SparseMatrix(m,r)

    for i in range(m):
      for j in range(r):
        el = 0
        for k in range(n):
          a = self.get_data_at(i,k) * other.get_data_at(k,j)
          el += a 
        product_matrix.insertLink(i,j,el)
    
    return product_matrix

  # return a string representation of the matrix
  def __str__ (self):
    s = ''
    current = self.matrix

    # if the matrix is empty return blank string
    if (current == None):
      return s

    for i in range (self.num_rows):
      for j in range (self.num_cols):
        if ((current != None) and (current.row == i) and (current.col == j)):
          s = s + str (current.data) + " "
          current = current.next
        else:
          s = s + "0 "
      s = s + "\n"
    return s

def readMatrix (inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = SparseMatrix (row, col)

  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    for j in range (col):
      elt = int(line[j])
      if (elt != 0):
        mat.insertLink (i, j, elt)
  line = inFile.readline()

  return mat

def main ():
  inFile = open ("matrix.txt", "r")

  print ("\nTest Matrix Addition")
  matA = readMatrix (inFile)
  print (matA)
  matB = readMatrix (inFile)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)
  
  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.setElement (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Element to Zero")
  matA.setElement (1, 1, 0)
  print (matA)

  print ("\nTest Getting a Row")
  row = matP.getRow(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.getCol(0)
  print (col)

  inFile.close()

main()




