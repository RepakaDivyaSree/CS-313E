#  File: ExpressionTree.py

#  Description: create expression tree

#  Student Name: Adam Roach

#  Student UT EID: abr875

#  Partner Name: Eun Seo

#  Partner UT EID: es29857

#  Course Name: CS 313E

#  Unique Number: 50945s

#  Date Created: 21 April 2016

#  Date Last Modified: 21 April 2016


class Stack (object):
	def __init__ (self):
		self.stack = []

	# add an item to the top of the stack
	def push (self, item):
		self.stack.append (item)

	# remove an item from the top of the stack
	def pop (self):
		return self.stack.pop()

	# check what is on top of the stack without removing it
	def peek (self):
		return self.stack[len(self.stack) - 1]

	# check if a stack is empty
	def is_empty (self):
		return (len(self.stack) == 0)

	# return the number of elements in the stack
	def size (self):
		return (len (self.stack))

def operate (oper1, oper2, token):
	if (token == "+"):
		return oper1 + oper2
	elif (token == "-"):
		return oper1 - oper2
	elif (token == "*"):
		return oper1 * oper2
	else:
		return oper1 / oper2

def rpn (s):
	theStack = Stack()

	operators = ['+', '-', '*', '/']

	tokens = s.split()

	for item in tokens:
		if (item in operators):
			oper2 = theStack.pop()
			oper1 = theStack.pop()
			theStack.push (operate (oper1, oper2, item))
		else:
			theStack.push (float(item))

	return theStack.pop()


class Node (object):
	def __init__ (self, data = None):
		self.data = data
		self.lchild = None
		self.rchild = None

class Tree (object):
	def __init__ (self):
		self.root = None

	# search for a node with a key
	def search (self, key):
		current = self.root
		while ((current != None) and (current.data != key)):
			if (key < current.data):
				current = current.lchild
			else:
				current = current.rchild
		return current
	'''
	# insert a node in a tree
	def insert (self, val):
		newNode = Node (val)

		if (self.root == None):
			self.root = newNode
		else:
			current = self.root
			parent = self.root
			while (current != None):
				parent = current
	if (val < current.data):
		current = current.lchild
	else:
		current = current.rchild
		if (val < parent.data):
			parent.lchild = newNode
		else:
			parent.rchild = newNode
	'''
	# in order traversal - left, center, right
	def inOrder (self, aNode):
		if (aNode != None):
			st = ''
			st += self.inOrder (aNode.lchild)
			if aNode.data != None:
				st += str(aNode.data) + ' '
			st += self.inOrder (aNode.rchild)
			return st 
		return ''

	# pre order traversal - center, left, right
	def preOrder (self, aNode):
		if (aNode != None):
			st = ''
			if aNode.data != None:
				st = str(aNode.data) + ' '
			st += self.preOrder (aNode.lchild)
			st += self.preOrder (aNode.rchild)
			return st
		return ''

	# post order traversal - left, right, center
	def postOrder (self, aNode):
		if (aNode != None):
			st = ''
			st += self.postOrder (aNode.lchild)
			st += self.postOrder (aNode.rchild)
			if aNode.data != None:
				st += str(aNode.data) + ' '
			return st 
		return '' 


	# delete a node with a given key
	def delete (self, key):
		deleteNode = self.root
		parent = self.root
		isLeft = False

		# if empty tree
		if (deleteNode == None):
			return False

		# find the delete node
		while ((deleteNode != None) and (deleteNode.data != key)):
			parent = deleteNode
			if (key < deleteNode.data):
				deleteNode = deleteNode.lchild
				isLeft = True
			else:
				deleteNode = deleteNode.rchild
				isLeft = False
				
		# if node not found
		if (deleteNode == None):
			return False

		# delete node is a leaf node
		if (deleteNode.lchild == None) and (deleteNode.rchild == None):
			if (deleteNode == self.root):
				self.root = None
			elif (isLeft):
						parent.lchild = None
			else:
				parent.rchild = None


def main():
	in_file = open ("expression.txt", "r")

	l = []

	for line in in_file:
		treeLine = line.strip()
		l.append(treeLine)

	for expression in l:
		tokens = expression.split()
		treeStack = Stack()
		expTree = Tree()
		expTree.root = Node()

		current = expTree.root

		operators = ['+', '-', '*', '/']

		for token in tokens:
			if (token == '('):		 
				current.lchild = Node()
				treeStack.push(current)
				current = current.lchild
			elif (token in operators):
				current.data = token
				treeStack.push(current)
				current.rchild = Node()
				current = current.rchild
			elif (token[0].isdigit() == True):
				current.data = eval(token)
				current = treeStack.pop()
			else:
				if (treeStack.is_empty() == False):
					current = treeStack.pop()


		prefix = expTree.preOrder(expTree.root)
		postfix = expTree.postOrder(expTree.root)

		value = rpn(postfix)


		print(expression + " = " + str(value))
		print("Prefix Expression:", prefix)
		print("Postfix Expression:", postfix)
		print()

	in_file.close()


main()