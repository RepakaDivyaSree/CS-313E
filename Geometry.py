#  File: Geometry.py

#  Description: program to  see geometry

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 02/20/2016

#  Date Last Modified: 02/20/2016

import math
class Point(object):
	def __init__ (self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __str__ (self):
		s = "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
		return s

	def distance (self, other):
		x = (self.x - other.x)**2
		y = (self.y - other.y)**2
		z = (self.z - other.z)**2
		return ((x+y+z)**0.5)
	
	# test for equality between two points
	def __eq__ (self, other):
		return (self.x == other.x and self.y == other.y and self.z == other.z)

class Sphere(object):
	# constructor with default values
	def __init__(self, x=0, y=0, z=0, radius = 1):
		self.center = Point(x, y, z)
		self.radius = radius

	def __str__(self):
		return "Center: " + str(self.center) + ", Radius: " + str(self.radius)

	# compute surface area of Sphere
	def area (self):
		sa = 4 * math.pi * self.radius**2
		return sa

	# compute volume of a Sphere
	def volume (self):
		vol = (4/3) * math.pi * self.radius**3
		return vol

	# determines if a Point is strictly inside the Sphere
	def is_inside_point (self, p):
		# even though distance under Point, can still use it?
		dist = p.distance(self.center)
		return (self.radius > dist)

	# determine if another Sphere is strictly inside this Sphere
	def is_inside_sphere (self, other):
		# dist = distance from self.center and other.center
		dist = self.center.distance(other.center)
		return (self.radius > (other.radius + dist))

	# determine if a Cube is strictly inside this Sphere
	# determine if the eight corners of the Cube are inside the Sphere
	def is_inside_cube(self, a_cube):
		dist = self.center.distance(a_cube.center)
		hypot_half = (((a_cube.side**2) + (a_cube.side**2))**0.5)/2
		return (self.radius >= dist + hypot_half)

	# determine if another Sphere intersects this Sphere
	# there is a non-zero volume of intersection
	def does_intersect_sphere (self, other):
		dist = self.center.distance (other.center)
		return (dist < (self.radius + other.radius))

	# determine if a Cube intersects this Sphere
	# there is a non-zero volume of intersection
	# there is at least one corner of the Cube in the Sphere
	def does_intersect_cube (self, a_cube):
		dist = self.center.distance(a_cube.center)
		hypot_half = (((a_cube.side**2) + (a_cube.side**2))**0.5)/2
		sum_radii = self.radius + hypot_half

		if (sum_radii <= dist) and (sum_radii >= dist): 
			return True
		else:
			return False

	 #### **** CHECKCHECK #### ****
	# return the largest Cube object that is circumscribed by this Sphere
	# all eight corners of the Cube are on the Sphere
	def circumscribe_cube (self):
		return ((2*self.radius) / (3**0.5))


class Cube(object):
	def __init__(self, x=0, y=0, z=0, side = 1):
		self.center = Point(x,y,z)
		self.side = side

	def __str__(self):
		return "Center: " + str(self.center) + ", Side: " + str(self.side)

	# compute surface area of Cube
	def area (self):
		sa = 6 * self.side**2
		return sa
 
	# compute volume of a Cube
	def volume (self):
		vol = self.side**3
		return vol

	# determines if a Point is strictly inside this Cube
	def is_inside_point (self, p):
		dist = p.distance(self.center)
		return (self.side > dist)		

	# determine if a Sphere is strictly inside this Cube or
	# determine if the smallest cube that contains the Sphere is within the Cube
	def is_inside_sphere (self, a_sphere):
		dist = self.center.distance(a_sphere.center)
		return ((self.side/2) > dist + a_sphere.radius) #and (hypot >= dist + a_sphere.radius)
	
	# determine if another Cube is strictly inside this Cube
	def is_inside_cube (self, other):
		dist = self.center.distance (other.center)
		return (dist + other.side < self.side)

	# determine if a Cylinder is strictly inside this Cube
	def is_inside_cylinder (self, a_cyl):
		return (a_cyl.height < self.side)

	# determine if another Cube intersects this Cube
	# there is a non-zero volume of intersection
	# there is at least one vertex of the other Cube
	# in this Cube
	def does_intersect_cube (self, other):
		dist = self.center.distance(other.center)
		return (dist < self.side + other.side)

	# determine the volume of intersection if this Cube 
	# intersects with another Cube
	def intersection_volume (self, other):
		return (self.volume() - other.volume())

	# return the largest Sphere object that is inscribed
	# by this Cube
	def inscribe_sphere (self):
		return self.center

class Cylinder (object):
	# Cylinder is defined by its center (which is a Point object),
	# radius and height. The main axis of the Cylinder is along the
	# z-axis and height is measured along this axis
	def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
		self.center = Point(x, y, z)
		self.radius = radius
		self.height = height

	# string representation of a Cylinder: Center: (x, y, z), Radius: value, Height: value
	def __str__ (self):
		return "Center: " + str(self.center) + ", Radius: " + str(self.radius) + ", Height: " + str(self.height)

	# compute surface area of Cylinder
	def area (self):
		sa = (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius**2)
		return sa

	# compute volume of a Cylinder
	def volume (self):
		vol = math.pi * self.radius**2 * self.height
		return vol
	
	# determine if a Point is strictly inside this Cylinder
	def is_inside_point (self, p):
		dist = p.distance(self.center)
		return ((self.radius > dist) and (self.height > dist))

	# determine if a Sphere is strictly inside this Cylinder
	def is_inside_sphere (self, a_sphere):
		dist = self.center.distance(a_sphere.center)
		return ((self.radius > (a_sphere.radius + dist)) and (self.radius > (a_sphere.height + dist)))
	
	# determine if a Cube is strictly inside this Cylinder
	# determine if all eight corners of the Cube are in the Cylinder
	def is_inside_cube (self, a_cube):
		dist = self.center.distance(a_cube.center)
		return (self.radius >= dist + a_cube.side)

	# determine if another Cylinder is strictly inside this Cylinder
	def is_inside_cylinder (self, other):
		dist = self.center.distance(other.center)
		return (self.radius > (other.radius + dist))

	# determine if another Cylinder intersects this Cylinder
	# there is a non-zero volume of intersection
	def does_intersect_cylinder (self, other):
		dist = self.center.distance (other.center)
		return (dist < (self.radius + other.radius)) and (dist < (self.height + other.height))

def main():
	# open file "geometry.txt" for reading
	in_file = open("geometry.txt", 'r')

	# read the coordinates of the first Point p
	# read first line
	p_coord = in_file.readline()
	# strip newline char
	p_coord = p_coord.strip()
	# split coordinates into single values
	p_coord = p_coord.split(" ")  
	# create list with only float values
	p_list = []
	for i in range (5):
		if (p_coord[i] != ""):
			p_list.append(float(p_coord[i]))

	# create a Point object and print its coordinates
	pointP = Point(p_list[0], p_list[1], p_list[2])
	print("Point p:", pointP)

	# read the coordinates of the second Point q
	q_coord = in_file.readline()
	q_coord = q_coord.strip()
	q_coord = q_coord.split(" ")

	q_list = []
	for i in range (5):
		if q_coord[i] != "":
			q_list.append(float(q_coord[i])) 

	# create a Point object and print its coordinates
	pointQ = Point(q_list[0], q_list[1], q_list[2])
	print("Point q:", pointQ)

	# read the coordinates of the center and radius of sphereA
	sphA_coord = in_file.readline()
	sphA_coord = sphA_coord.strip()
	sphA_coord = sphA_coord.split(" ")

	sphA_list = []
	for i in range (5):
		if sphA_coord[i] != "":
			sphA_list.append(float(sphA_coord[i])) 

	# create a Sphere object and print it
	sphereA = Sphere(sphA_list[0], sphA_list[1], sphA_list[2], sphA_list[3])
	print("sphereA:", sphereA)

	# read the coordinates of the center and radius of sphereB
	sphB_coord = in_file.readline()
	sphB_coord = sphB_coord.strip()
	sphB_coord = sphB_coord.split(" ")

	sphB_list = []
	for i in range (5):
		if sphB_coord[i] != "":
			sphB_list.append(float(sphB_coord[i])) 

	# create a Sphere object and print it
	sphereB = Sphere(sphB_list[0], sphB_list[1], sphB_list[2], sphB_list[3])
	print("sphereB:", sphereB)

	# read the coordinates of the center and side of cubeA
	cubeA_coord = in_file.readline()
	cubeA_coord = cubeA_coord.strip()
	cubeA_coord = cubeA_coord.split(" ")

	cubeA_list = []
	for i in range (5):
		if cubeA_coord[i] != "":
			cubeA_list.append(float(cubeA_coord[i])) 

	# create a Cube object and print it
	cubeA = Cube(cubeA_list[0], cubeA_list[1], cubeA_list[2], cubeA_list[3])
	print("cubeA:", cubeA)
  
	# read the coordinates of the center and side of cubeB
	cubeB_coord = in_file.readline()
	cubeB_coord = cubeB_coord.strip()
	cubeB_coord = cubeB_coord.split(" ")

	cubeB_list = []
	for i in range (5):
		if cubeB_coord[i] != "":
			cubeB_list.append(float(cubeB_coord[i])) 

	# create a Cube object and print it
	cubeB = Cube(cubeB_list[0], cubeB_list[1], cubeB_list[2], cubeB_list[3])
	print("cubeB:", cubeB)

	cylA_coord = in_file.readline()
	cylA_coord = cylA_coord.strip()
	cylA_coord = cylA_coord.split(" ")

	cylA_list = []
	for i in range (5):
		if cylA_coord[i] != "":
			cylA_list.append(float(cylA_coord[i])) 

	# create a Cylinder object and print it
	cylA = Cylinder(cylA_list[0], cylA_list[1], cylA_list[2], cylA_list[3], cylA_list[4])
	print(cylA)

	# read the coordinates of the center, radius and height of cylB
	cylB_coord = in_file.readline()
	cylB_coord = cylB_coord.strip()
	cylB_coord = cylB_coord.split(" ")

	cylB_list = []
	for i in range (5):
		if cylB_coord[i] != "":
			cylB_list.append(float(cylB_coord[i])) 

	# create a Cylinder object and print it
	cylB = Cylinder(cylB_list[0], cylB_list[1], cylB_list[2], cylB_list[3], cylB_list[4])
	print(cylB)

	# close file geometry.txt
	in_file.close()
	print()

	# print distance between p and q
	print("Distance between p and q:", pointQ.distance(pointP))
	print()

	# print area of sphereA
	print("Area of sphereA:", sphereA.area())

	# print volume of sphereA
	print("Volume of sphereA:", sphereA.volume())

	# print if Point p is inside sphereA
	if ((sphereA.is_inside_point(pointP)) == True):
		print ("Point p is inside sphereA")
	else:
		print ("Point p is not inside sphereA")
	
	# print if sphereB is inside sphereA
	if ((sphereA.is_inside_sphere(sphereB)) == True):
		print ("sphereB is inside sphereA")
	else:
		print ("sphereB is not inside sphereA")

	# print if cubeA is inside sphereA
	if ((sphereA.is_inside_cube(cubeA)) == True):
		print ("cubeA is inside sphereA")
	else:
		print ("cubeA is not inside sphereA")

	# print if sphereA intersects with sphereB
	if ((sphereB.does_intersect_sphere(sphereA)) == True):
		print ("sphereA does intersect sphereB")
	else:
		print ("sphereA is not inside sphereB")


	# print if cubeB intersects with sphereB
	if ((sphereB.does_intersect_cube(cubeB)) == True):
		print ("cubeB does intersect sphereB")
	else:
		print ("cubeB does intersect sphereB")

	print("Largest Cube circumscribed by sphereA:", sphereA, ", Side:", sphereA.circumscribe_cube())
	print()

	# print area of cubeA
	print("Area of cubeA:", cubeA.area())

	# print volume of cubeA
	print("Volume of sphereA:", cubeA.volume())

	# print if Point p is inside cubeA
	if ((cubeA.is_inside_point(pointP)) == True):
		print("Point p is inside cubeA")
	else:
		print("Point p is not inside cubeA")

	# print if sphereA is inside cubeA
	if ((cubeA.is_inside_sphere(sphereA)) == True):
		print("sphereA is inside cubeA")
	else:
		print("sphereA is not inside cubeA")

	# print if cubeB is inside cubeA
	if ((cubeA.is_inside_cube(cubeB)) == True):
		print ("cubeB is inside cubeA")
	else:
		print ("cubeB is not inside cubeA")		

	# print if cylA is inside cubeA
	if ((cubeA.is_inside_cylinder(cylA)) == True):
		print ("cylA is inside cubeA")
	else:
		print ("cylA is not inside cubeA")

	# print if cubeA intersects with cubeB
	if ((cubeA.does_intersect_cube(cubeB)) == True):
		print ("cubeA does intersect cubeB")
	else:
		print ("cubeA does not intersect cubeB")		
	

	# print the intersection volume of cubeA and cubeB
	print("Intersection volume of cubeA and cubeB:", cubeA.intersection_volume(cubeB))

	# print the largest Sphere object inscribed by cubeA
	print("Largest Sphere inscribed by cubeA:", cubeA.inscribe_sphere(), "Radius:", sphereA.radius/2)
	
	# print area of cylA

	print()
	print("Area of cylA:", cylA.area())

	# print volume of cylA
	print("Volume of cylA:", cylA.volume())

# print if Point p is inside cylA
	if ((cylA.is_inside_point(pointP)) == True):
		print("Point p is inside cylA")
	else:
		print("Point p is not inside cylA")
	
	# print if sphereA is inside cylA
	if ((cylA.is_inside_sphere(sphereA)) == True):
		print("sphereA is inside cylA")
	else:
		print("sphereA is not inside cylA")
			
	# print if cubeA is inside cylA
	if ((cylA.is_inside_cube(cubeA)) == True):
		print("cubeA is inside cylA")
	else:
		print("cubeA is not inside cylA")	
			
	# print if cylB is inside cylA
	if ((cylA.is_inside_cylinder(cylB)) == True):
		print("cylB is inside cylA")
	else:
		print("cylB is not inside cylA")	
			
	# print if cylB intersects with cylA
	if ((cylA.does_intersect_cylinder(cylB)) == True):
		print("cylA does intersect cylB")
	else:
		print("cylA does not intersect cylB")

main()