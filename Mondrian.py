#  File: Mondrian.py

#  Description: program to draw negative circles with recursive pentagons

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 03/05/2016

#  Date Last Modified: 03/05/2016

import turtle
import random

def drawPentagon(ttl, n2):
  for k in range (0, 5):
    ttl.pendown()
    ttl.forward(n2)
    ttl.left(72)
    #ttl.forward(n2)
    ttl.penup()

def drawStar(ttl, n2):
  for k in range (0, 2):
    ttl.pendown()
    ttl.forward(15)
    ttl.left(180)
    ttl.penup()

def recurShape(shape, ttl, n, n2):
  for i in range (0, n):
    shape(ttl, n2)
    ttl.left(28)
  ttl.penup()
  ttl.forward(100)

def randomPoint():
  x = random.randint(0, 200)
  return x

def main():
  # ask user for # of iterations
  iters = int(input("Enter a level of recursion between 0 and 20: "))

  if (iters < 0):
    if (iters > 20):
      iters = int(input("Enter a level of recursion between 0 and 20: "))

  # set up screen size
  turtle.setup (800, 800, 0, 0)

  # create turtle object
  turtle.bgcolor("beige")

  # create turtle object
  ttl = turtle.Turtle()

  # set turtle speed
  ttl.speed(10)

  # call recursive function to draw negative space circle with recursive pentagons
  colorList = ["light slate blue", "medium aquamarine", "salmon"]

  bigNumList = [200, 100, 200]

  for i in range (0, 3):
    ttl.color(colorList[i])
    recurShape(drawPentagon, ttl, iters, bigNumList[i])
    ttl.goto(randomPoint(), randomPoint())

  # draw cute stars
  for j in range (0, 5):
    ttl.color("red")
    recurShape(drawStar, ttl, iters, 10)
    ttl.goto(randomPoint(), randomPoint())

  pic = ttl.getscreen()
  pic.getcanvas().postscript(file = 'Mondrian.eps')

  # persist drawing
  turtle.done()
  
main()
