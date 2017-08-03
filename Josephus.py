#  File: Josephus.py

#  Description: This program uses a circular linked list to solve the Josephus problem

#  Student Name: Marion Milloy

#  Student UT EID: mm69994

#  Partner Name: Eun Seo

#  Partner UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 4/9/16

#  Date Last Modified: 4/9/16

class Link(object):
	# Constructor
	def __init__ (self, data, next = None):
		self.data = data
		self.next = next


class CircularList(object):
	# Constructor
	def __init__ (self): 
		self.first = None

	# Insert an element in the list
	def insert (self, item):
		# create a new Link object
		newLink = Link(item)
		# set its address
		current = self.first

		# there is no link
		if (current == None):
			# set link address to itself
			self.first = newLink
			newLink.next = newLink
			
			return

		while (current.next != self.first):
			current = current.next

		#(current.next == self.first):
		current.next = newLink
		newLink.next = self.first

	# Find the link with the given key
	def find (self, key):
		current = self.first

		while (current.data != key):
			current = current.next

		return current

  # Delete a link with a given key
	def delete (self, key):
		current = self.first
		previous = self.first
	
		# if list empty return none
		if (current == None):
			return None

		# while we haven't fully circled the list
		while (previous.next != self.first):
			previous = previous.next

		# (previous.next == self.first)
		# returned to where we started
		# clook for link with matching key value
		while (current.data != key):
			previous = current
			current = current.next

		#(current.data == key)
		if (self.first != self.first.next):
			# continue traversing
			self.first = current.next
		# (self.first == self.first.next)
		else:
			self.first = None

		# because you have deleted the link, now you need
		# to connect the previous link to the next link
		previous.next = current.next


	# Delete the nth link starting from the Link start 
	# Return the next link from the deleted Link
	def deleteAfter (self, start, n):
		current = self.find(start)

		for i in range (1, n):
			current = current.next

		print(str(current.data), end = ' ')
		
		self.delete(current.data)

		return current.next

	# Return a string representation of a Circular List
	def __str__ (self):
		s = ""
		current = self.first

		# traverse until we reach the starting link
		while (current.next != self.first):
			s += str(current.data) + " "
			current = current.next

		# when current.next == self.first, return the string
		return s

def main():
	# open file for reading
	in_file = open("josephus.txt", "r")

	# read in the number of soldiers
	num_soldiers = int(in_file.readline())

	# read in the soldier where the counting starts
	count_start = int(in_file.readline())

	# read in the elimination number
	n = int(in_file.readline())

	# close the file
	in_file.close()

	# create a circular list object
	# with links from 1 to the number of soldiers
	soldiers_lst = CircularList()

	for i in range (1, num_soldiers + 1):
		soldiers_lst.insert(i) # initialize list with 'names' (values 1-N)

	# point pointers at start of list
	# pointing at position from where we wnat to start 
	# the couting of the list

	# continue until there is only 1 person left
	# count up to n times and remove the element
	for i in range (1, num_soldiers):
		count_start = soldiers_lst.deleteAfter(count_start, n)
		# move pointer n times
		count_start = count_start.data

	print()

	for i in range (num_soldiers + 1, num_soldiers + 2):
		count_start = soldiers_lst.deleteAfter(count_start, n)
		# move pointer n times
		count_start = count_start.data

	print()

main()