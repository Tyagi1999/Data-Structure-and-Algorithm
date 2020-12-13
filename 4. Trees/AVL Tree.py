class Node():
	def __init__(self, data):
		self.data = data
		self.height = 0
		self.left = None
		self.right = None

class AVL():
	def __init__(self):
		self.root = None
	
	def CalcHeight(self, node):
		if not node:
			return -1
		return node.height
	
	def CalcBalance(self, node):
		if not node:
			return 0
		return self.CalcHeight(node.left) - self.CalcHeight(node.right)
	
	def insert(self, data):
		self.root = self.insertNode(data, self.root)
	
	def insertNode(self, data, node):
		if not node:
			return Node(data)
		if data < node.data:
			node.left = self.insertNode(data, node.left)
		else:
			node.right = self.insertNode(data, node.right)
		node.height = max(self.CalcHeight(node.left), self.CalcHeight(node.right)) + 1
		return self.settleViolation(data, node)
		
	def settleViolation(self, data, node):
		balance = self.CalcBalance(node)
		if balance > 1 and data < node.left.data:
			print("Left left situation...")
			return self.rotateRight(node)
		if balance < -1 and data > node.right.data:
			print("Right right situation...")
			return self.rotateLeft(node)
		if balance > 1 and data > node.left.data:
			print("Left right situation...")
			node.left = self.rotateLeft(node.left)
			return self.rotateRight(node)
		if balance < -1 and data < node.right.data:
			print("Right left situation...")
			node.right = self.rotateRight(node.right)
			return self.rotateLeft(node)
		return node
		
	def traverse(self):
		if self.root:
			self.traverseInorder(self.root)
	
	def traverseInorder(self, node):
		if node.left:
			self.traverseInorder(node.left)
		print("%s" %node.data)
		if node.right:
			self.traverseInorder(node.right)
		
	def rotateRight(self, node):
		print("Rotating to the right on node ", node.data)
		tempLeft = node.left
		t = tempLeft.right
		tempLeft.right = node
		node.left = t
		node.height = max(self.CalcHeight(node.left), self.CalcHeight(node.right)) + 1
		tempLeft.height = max(self.CalcHeight(tempLeft.left), self.CalcHeight(tempLeft.right)) + 1
		return tempLeft
		
	def rotateLeft(self, node):
		print("Rotating to the left on node", node.data)
		tempRight = node.right
		t = tempRight.left
		tempRight.left = node
		node.right = t
		node.height = max(self.CalcHeight(node.left), self.CalcHeight(node.right)) + 1
		tempRight.height = max(self.CalcHeight(tempRight.left), self.CalcHeight(tempRight.right)) + 1
		return tempRight
	
	def removeNode(self, data, node):
		if not node:
			return node
		if data < node.data:
			node.left = self.removeNode(data, node.left)
		elif data > node.data:
			node.right = self.removeNode(data, node.right)
		else:
			if not node.left and not node.right:
				print("Removing leaf node...")
				del node
				return None
			if not node.left:
				print("Removing right child...")
				tempNode = node.right
				del node
				return tempNode
			elif not node.right:
				print("Removing left child...")
				tempNode = node.left
				del node
				return tempNode
			print("Removing node with 2 child...")
			tempNode = self.getPredecessor(node.left)
			node.data = tempNode.data
			node.left = self.removeNode(tempNode.data, node.left)
		if not node:
			return node
		node.height = max(self.CalcHeight(node.left), self.CalcHeight(node.right)) + 1
		balance = self.CalcBalance(node)
		if balance > 1 and self.CalcBalance(node.left) >= 0:
			return self.rotateRight(node)
		if balance > 1 and self.CalcBalance(node.left) < 0:
			node.left = self.rotateLeft(node.left)
			return self.rotateRight(node)
		if balance < -1 and self.CalcBalance(node.right) <= 0:
			return self.rotateLeft(node)
		if balance < -1 and self.CalcBalance(node.right) > 0:
			node.right = self.rotateRight(node.right)
			return self.rotateLeft(node)
		return node
		
	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root)
	
	def getPredecessor(self, node):
		if node.right:
			return self.getPredecessor(node.right)
		return node
		
avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(6)
avl.insert(15)

avl.traverse()

avl.remove(15)
avl.remove(20)

avl.traverse()