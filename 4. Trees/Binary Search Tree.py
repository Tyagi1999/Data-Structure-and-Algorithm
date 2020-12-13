class Node():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
	
class BinarySearchTree():
	def __init__(self):
		self.root = None
	
	def insert(self, data):
		if self.root == None:
			self.root = Node(data)
		else:
			self.insertion(data, self.root)
	
	def insertion(self, data, node):
		if data < node.data:
			if node.left == None:
				node.left = Node(data)
			else:
				self.insertion(data, node.left)
		else:
			if node.right == None:
				node.right = Node(data)
			else:
				self.insertion(data, node.right)
	
	def removal(self, data, node):
		if not node:
			return node
		if data < node.data:
			node.left = self.removal(data, node.left)
		elif data > node.data:
			node.right = self.removal(data, node.right)
		else:
			if not node.left and not node.right:
				print("Removing leaf node...")
				del node
				return None
			if not node.left:
				print("Removing a node with single right child...")
				tempNode = node.right
				del node
				return tempNode
			elif not node.right:
				print("Removing a node with single left child...")
				tempNode = node.left
				del node
				return tempNode
			print("Removing node with two children...")
			tempNode = self.getPredecessor(node.left)
			node.data = tempNode.data
			node.left = self.removal(tempNode.data, node.left)
		return node
		
	def getPredecessor(self, node):
		if node.right:
			return self.getPredecessor(node.right)
		return node
		
	def remove(self, data):
		if self.root == None:
			return "Tree is empty"
		elif self.root:
			self.root = self.removal(data, self.root)
	
	def getMinValue(self):
		if self.root:
			return self.getMin(self.root)
		
	def getMin(self, node):
		if node.left:
			return self.getMin(node.left)
		return node.data
	
	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root)
		
	def getMax(self, node):
		if node.right:
			return self.getMax(node.right)
		return node.data
	
	def inOrderTraversal(self):
		if self.root:
			self.traverseInOrder(self.root)
	
	def traverseInOrder(self, node):
		if node.left:
			self.traverseInOrder(node.left)
		print(node.data, end = " ")
		if node.right:
			self.traverseInOrder(node.right)
	
	def preOrderTraversal(self):
		if self.root:
			self.traversePreOrder(self.root)
	
	def traversePreOrder(self, node):
		print(node.data, end = " ")
		if node.left:
			self.traversePreOrder(node.left)
		if node.right:
			self.traversePreOrder(node.right)
		
	def postOrderTraversal(self):
		if self.root:
			self.traversePostOrder(self.root)
	
	def traversePostOrder(self, node):
		if node.left:
			self.traversePostOrder(node.left)
		if node.right:
			self.traversePostOrder(node.right)
		print(node.data, end = " ")
		
bst = BinarySearchTree()
bst.insert(10)
bst.insert(6)
bst.insert(15)
bst.insert(2)
bst.insert(9)
bst.insert(12)
bst.insert(20)

bst.inOrderTraversal()
print()
print("----------------------------------")
bst.preOrderTraversal()
print()
print("----------------------------------")
bst.postOrderTraversal()
print()
print("----------------------------------")
print("Minimum is: ",bst.getMinValue())
print("----------------------------------")
print("Maximum is: ",bst.getMaxValue())
print("----------------------------------")
bst.remove(9)
bst.remove(15)
bst.inOrderTraversal()
print()
print("----------------------------------")
bst.preOrderTraversal()
print()
print("----------------------------------")
bst.postOrderTraversal()		
