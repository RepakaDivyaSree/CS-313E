#  File: Work.py

#  Description: program to calculate how many lines of code Vyasa can write

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 03/25/2016

#  Date Last Modified: 03/26/2016

# modified Binary Search function
def modBinarySearch(n, k, lo, hi):
	# n = 59
	# k = 9

	v_sum = 0
	p = 0

	# make sure lo does not converge with hi
	while (hi > lo):
		# find average
		mid = (lo + hi) // 2
		# call helper function, see if what Vyasa has written is enough
		# set v = mid
		if (enough(mid, n, k) == 1):
			# set v = mid - 1
			if (enough(mid - 1, n, k) == 0):
				# yes, Vyasa has written enough, output mid (correct v)
				return mid
			# can Vyasa write less lines of code?
			else:
				hi = mid
		# no, Vyasa must continue writing--not enough lines
		else:
			# --point B--
			lo = mid

# helper function to test if Vyasa has written enough lines of code
def enough (v, n, k):
	p = 1
	finished = v
	# initialize continue
	cont = 1

	while (cont == 1):
		vyasa_wrote = v // (k ** p)
		if (vyasa_wrote == 0):
			#  if additional hours don't add value, leave while loop
			cont = 0
			# yes, V has finished so return 1
			if (finished >= n):
				return 1
			# sadly, V has not finished--mus go back to modBinarySearch function
			else:
				# --point B--
				return 0
		# sum up number of lines V has written
		else:
			finished = finished + vyasa_wrote
			p = p + 1

def main():
	# read file
	in_file = open("work.txt", 'r')

	# read num of data sets n you will have
	num_lines = in_file.readline()
	num_lines = int(num_lines)
	# while there are enough data sets
	for i in range(0, num_lines):
		# get n and k
		line = in_file.readline()
		line = line.strip()
		
		n, k = line.split(" ")
		
		n = int(n)
		k = int(k)
		
		# send to recurBinary function
		lo = 1
		hi = n

		# call recurBinary function		
		print(modBinarySearch(n, k, lo, hi))
main()
