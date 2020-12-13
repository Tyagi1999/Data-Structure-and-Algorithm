class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None
	
class DoubleLinkedList():
	def __init__(self):
		self.head = None
		self.size = 0
	
	def insertAtStart(self, data):
		newNode = Node(data)
		self.size += 1
		if self.head == None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head.previous = newNode
			self.head = newNode
	
	def insertAtEnd(self, data):
		newNode = Node(data)
		currentNode = self.head
		self.size += 1
		while currentNode.next != None:
			currentNode = currentNode.next
		currentNode.next = newNode
		newNode.previous = currentNode
	
	def traverse(self):
		currentNode = self.head
		while currentNode.next != None:
			print(currentNode.data, end="")
			print(" --> ", end="")
			currentNode = currentNode.next
		print(currentNode.data)
		
	def traverseReverse(self):
		currentNode = self.head
		while currentNode.next != None:
			currentNode = currentNode.next
		while currentNode.previous != None:
			print(currentNode.data, end="")
			print(" <-- ", end="")
			currentNode = currentNode.previous
		print(currentNode.data)
	
	def lengthLinkedList(self):
		return self.size
	
	def removeData(self, data):
		prevNode = None
		currNode = self.head
		while currNode.data != data:
			prevNode = currNode
			currNode = currNode.next
		if prevNode == None:
			self.head = currNode.next
			currNode.next = None
			self.head.previous = None
			self.size -= 1
		elif currNode.next == None:
			prevNode.next = None
			self.size -= 1
		else:
			prevNode.next = currNode.next
			currNode.next.previous = prevNode
			self.size -= 1

doublelinkedlist = DoubleLinkedList()

doublelinkedlist.insertAtStart(2)
doublelinkedlist.insertAtStart(4)
doublelinkedlist.insertAtStart(6)
doublelinkedlist.insertAtEnd(8)

print("Size of linked list: ", doublelinkedlist.lengthLinkedList())

print("Traversal from start: ")
doublelinkedlist.traverse()

print("Traversal from end: ")
doublelinkedlist.traverseReverse()

doublelinkedlist.removeData(8)
doublelinkedlist.removeData(4)

print("Size after removing the data: ", doublelinkedlist.lengthLinkedList())

print("Traversal from start: ")
doublelinkedlist.traverse()

print("Traversal from end: ")
doublelinkedlist.traverseReverse()

