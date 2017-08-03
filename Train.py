#  File: Train.py

#  Description: program to draw train

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 02/23/2016

#  Date Last Modified: 02/27/2016

import turtle

def drawCircle (ttl, x, y, radius, extent, steps):
	ttl.penup()
	ttl.pensize(2)
	ttl.color('red')

	ttl.goto(x, y)
	ttl.pendown()
	ttl.circle(radius)
	ttl.penup()

def drawWhiteCircle (ttl, x, y, radius, extent, steps):
	ttl.penup()
	ttl.pensize(2)
	ttl.pencolor('red')
	ttl.fillcolor('white')

	ttl.begin_fill()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.circle(radius)
	ttl.penup()
	ttl.end_fill()

def drawLine(ttl, x1, y1, x2, y2, tilt, color):
	ttl.penup()
	ttl.pensize(2)
	ttl.color(color)

	ttl.goto(x1, y1)
	ttl.pendown()
	ttl.goto(x2, y2)
	ttl.penup()

	ttl.tilt(90)

def dottedLine(ttl, length_line, length_dot, length_space):
	ttl.pencolor('black')
	ttl.forward(6)
	for i in range(length_line):
		ttl.pendown()
		ttl.forward(length_dot)
		ttl.penup()
		ttl.forward(length_space)

def drawRectangle (ttl, x1, y1, x2, y2, x3, y3, x4, y4, tilt):
	ttl.penup()
	ttl.pensize(2)
	ttl.color('blue')

	ttl.goto(x1, y1)
	ttl.pendown()
	ttl.goto(x2, y2)
	ttl.penup()

	ttl.tilt(90)

	ttl.penup()
	ttl.goto(x2, y2)
	ttl.pendown()
	ttl.goto(x3, y3)
	ttl.penup()

	ttl.tilt(90)

	ttl.penup()
	ttl.goto(x3, y3)
	ttl.pendown()
	ttl.goto(x4, y4)
	ttl.penup()

	ttl.tilt(90)

	ttl.penup()
	ttl.goto(x4, y4)
	ttl.pendown()
	ttl.goto(x1, y1)
	ttl.penup()

def drawWindows (ttl, x1, y1, x2, y2, x3, y3, x4, y4, tilt):
	ttl.penup()
	ttl.pensize(2)
	ttl.color('blue')
	ttl.fillcolor('gray')
	ttl.begin_fill()

	ttl.goto(x1, y1)
	ttl.pendown()
	ttl.goto(x2, y2)
	ttl.penup()

	ttl.tilt(90)

	ttl.penup()
	ttl.goto(x2, y2)
	ttl.pendown()
	ttl.goto(x3, y3)
	ttl.penup()

	ttl.tilt(90)

	ttl.penup()
	ttl.goto(x3, y3)
	ttl.pendown()
	ttl.goto(x4, y4)
	ttl.penup()

	ttl.tilt(90)

	ttl.penup()
	ttl.goto(x4, y4)
	ttl.pendown()
	ttl.goto(x1, y1)
	ttl.penup()
	
	ttl.end_fill()


def trackRidges(ttl, x1, y1, x2, y2, x3, y3, x4, y4, tilt, color):
	for iter in range (13):
		ttl.penup()
		ttl.pensize(2)
		ttl.color(color)

		ttl.goto(x1, y1)
		ttl.pendown()
		ttl.goto(x2, y2)
		ttl.penup()

		ttl.tilt(90)

		ttl.penup()
		ttl.goto(x2, y2)
		ttl.pendown()
		ttl.goto(x3, y3)
		ttl.penup()

		ttl.tilt(90)

		ttl.penup()
		ttl.goto(x3, y3)
		ttl.pendown()
		ttl.goto(x4, y4)
		ttl.penup()

		ttl.tilt(90)

		ttl.penup()
		ttl.goto(x4, y4)
		ttl.pendown()
		ttl.goto(x1, y1)
		ttl.penup()

		x1 += 60
		x2 += 60
		x3 += 60
		x4 += 60

def drawSpokes(ttl, x1, x2, angle, length):
	for i in range (8):
		for j in range (2):
			ttl.penup()
			ttl.goto(x1, x2)
			ttl.setheading(angle)
			ttl.pendown()
			ttl.forward(length)
			ttl.penup()
			angle += 10
		angle += 25


def main():
	# set up screen size
	turtle.setup (800, 800, 0, 0)

	# create turtle object
	ttl = turtle.Turtle()
	
	# skinny bar
	drawLine(ttl, -395, 150, -175, 150, 90, 'blue')
	#ttl.tilt(90)
	drawLine(ttl, -175, 150, -175, 160, 90, 'blue')
	#ttl.tilt(90)
	drawLine(ttl, -175, 160, -395, 160, 90, 'blue')
	#ttl.tilt(90)
	drawLine(ttl, -395, 160, -395, 150, 90, 'blue')

	# draw left body
	ttl.goto(-375, 150)
	ttl.pendown()
	ttl.goto(-375, -65)
	ttl.tilt(90)
	ttl.goto(-350, -65)

	# draw 1st half circle
	ttl.left(90)
	ttl.circle(-60, 180)
	ttl.goto(-200, -65)

	ttl.left(90)
	ttl.goto(-200, 150)
	ttl.goto(-200, 100)

	ttl.left(90)
	ttl.goto(175, 100)
	ttl.right(90)
	ttl.goto(175, 25)
	ttl.right(90)
	ttl.goto(-200, 25)

	ttl.right(90)
	ttl.goto(-200, 15)
	ttl.right(90)
	ttl.goto(175, 15)

	ttl.left(90)
	ttl.goto(175,15)
	ttl.left(90)
	ttl.goto(-200,15)
	ttl.left(90)
	ttl.goto(-200,-65)
	ttl.left(90)
	ttl.goto(-150,-65)

	# draw 2nd half circle
	ttl.left(-0)
	ttl.circle(-50, 180)
	ttl.goto(10, -65)
	
	# draw 3rd half circle
	ttl.left(180)
	ttl.circle(-50, 180)
	ttl.goto(175, -65)
	ttl.penup()
	
	# draw last vertical line to finish up main train shape
	
	drawLine(ttl, 175, 100, 175, -90, None, 'blue')
	drawLine(ttl, 175, -90, 252, -90, None, 'blue')
	
	# draw angled botton piece
	ttl.left(45)
	ttl.pendown()
	ttl.goto(225,-50)
	drawLine(ttl, 225, -50, 175, -50, None, 'blue')

	# draw right layered nose
	drawRectangle (ttl, 175, -35, 200, -35, 200, 80, 175, 80, 90)
	drawRectangle (ttl, 200, 0, 210, 0, 210, 50, 200, 50, 90)
	
	# draw spout
	ttl.penup()
	ttl.goto(65, 100)
	
	ttl.pendown()
	ttl.goto(45,160)

	ttl.goto(55, 180)
	
	ttl.goto(55, 180)
	ttl.penup()

	ttl.heading()
	ttl.goto(55,180)
	ttl.pendown()
	ttl.goto(110, 180)
	ttl.goto(120, 160)
	ttl.goto(100, 100)
	ttl.penup()

	ttl.goto(45,160)
	ttl.heading()
	ttl.pendown()
	ttl.goto(120,160)
	ttl.penup()
	# END NOSE #

	
	# draw set of 2 vertical bars w/ dots
	ttl.goto(0,0)
	ttl.pendown()
	drawLine(ttl,-100, 100, -90, 100, None, 'blue')
	drawLine(ttl,-90, 100, -90, 25, None, 'blue')
	drawLine(ttl,-90, 25, -100, 25, None, 'blue')
	drawLine(ttl,-100, 25, -100, 100, None, 'blue')

	ttl.penup()
	ttl.goto(75, 10)
	ttl.pendown()
	drawLine(ttl, 75, 100, 85, 100, None, 'blue')
	drawLine(ttl, 85, 100, 85, 25, None, 'blue')
	drawLine(ttl, 85, 25, 75, 25, None, 'blue')
	drawLine(ttl, 75, 25, 75, 100, None, 'blue')
	ttl.penup()
	
	# ---- START 2 SHORT DOTTED LINES ---- #
	#dottedLine(ttl, length_line, length_dot, length_space):
	ttl.goto(-95,105)
	ttl.setheading(-90)
	ttl.pensize(5)
	dottedLine(ttl, 10, 1, 7)
	ttl.penup()

	ttl.goto(80,105)
	ttl.setheading(-90)
	ttl.pensize(5)
	dottedLine(ttl, 10, 1, 7)
	ttl.penup()

	# long dotted line
	ttl.goto(-200,20)
	ttl.setheading(0)
	ttl.pensize(5)
	dottedLine(ttl, 46, 1, 7)
	# ---- END DOTTED LINES ---- #
	
	
	# ---- DRAW WINDOWS ---- #
	drawWindows (ttl, -350, 125, -300, 125, -300, 65, -350, 65, 90)
	drawWindows (ttl, -275, 125, -225, 125, -225, 65, -275, 65, 90)
	# ---- END WINDOWS ---- #
	

	
	# ---- DRAW Spout1 ---- #
	#drawWindows (ttl, x1, y1, x2, y2, x3, y3, x4, y4, tilt):
	drawRectangle (ttl, -75, 125, -25, 125, -25, 100, -75, 100, 90)
	drawRectangle (ttl, -65, 135, -35, 135, -35, 125, -65, 125, 90)
	# ---- END Spout1 ---- #
	

	# ---- DRAW Black Train Tracks ---- #
	
	ttl.pencolor('black')
	ttl.pensize('2')
	drawLine(ttl, -395, -115, 380, -115, None, 'black')

	drawLine(ttl, -395, -125, 380, -125, None, 'black')
	
	# draw track ridges
	trackRidges(ttl, -380, -125, -380, -130, -355, -130, -355, -125, 90, 'black')
	
	# ---- END track ridges ---- #
	

	# 1ST RED CIRCLE
	# starts at right middle, go up counter clockwise
	
	ttl.penup()
	ttl.setheading(0)
	ttl.goto(-290,-15)
	# 1st large circle, outside
	drawCircle (ttl, -290, -15, -50, None, 300)
	# 1st circle, inner
	drawCircle (ttl, -290, -25, -40, None, 300)	
	drawSpokes(ttl, -290, -64, 80, 40)
	drawWhiteCircle (ttl, -295, -58, -8, None, 300)
	

	#  2ND RED CIRCLE
	ttl.penup()
	ttl.setheading(0)
	ttl.goto(-88,-30)
	# 1st large circle, outside
	drawCircle (ttl, -100, -35, -40, None, 100)
	# 1st circle, inner
	drawCircle (ttl, -99, -45, -30, None, 100)
	drawSpokes(ttl, -99, -74, 80, 29)
	drawWhiteCircle (ttl, -103, -70, -7, None, 100)
	
	#  3RD RED CIRCLE
	ttl.penup()
	ttl.setheading(0)
	ttl.goto(80,-30)
	# 1st large circle, outside
	drawCircle (ttl, 60, -35, -40, None, 100)
	# 1st circle, inner
	drawCircle (ttl, 60, -45, -30, None, 100)
	drawSpokes(ttl, 60, -74, 80, 29)
	drawWhiteCircle (ttl, 56, -70, -7, None, 100)

	# persist drawing	
	turtle.done()
main()