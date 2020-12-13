class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class SingleLinkedList():
	def __init__(self):
		self.size = 0
		self.head = None
	
	def insertAtStart(self, data):
		newNode = Node(data)
		self.size += 1
		if self.head == None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode
	
	def insertAtEnd(self, data):
		newNode = Node(data)
		currentNode = self.head
		self.size += 1
		while currentNode.next != None:
			currentNode = currentNode.next
		currentNode.next = newNode
	
	def lengthLinkedList(self):
		return self.size
	
	def traverse(self):
		currentNode = self.head
		while currentNode.next != None:
			print(currentNode.data)
			currentNode = currentNode.next
		print(currentNode.data)
	
	def removeData(self, data):
		previousNode = None
		currentNode = self.head
		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.next
		if previousNode == None:
			self.head = currentNode.next
		else:
			previousNode.next = currentNode.next
		self.size -= 1
	
	def lastToFirst(self):
		currentNode = self.head
		previousNode = None
		while currentNode.next != None:
			previousNode = currentNode
			currentNode = currentNode.next
		previousNode.next = None
		currentNode.next = self.head
		self.head = currentNode
		
		
linkedlist = SingleLinkedList()
linkedlist.insertAtStart(2)
linkedlist.insertAtStart(4)
linkedlist.insertAtStart(6)
linkedlist.insertAtEnd(8)
linkedlist.lastToFirst()
print("Size of linked list before delete: ", linkedlist.lengthLinkedList())
print("Traversing the linked list: ")
linkedlist.traverse()
linkedlist.removeData(4)
print("Size of linked list after deletion: ", linkedlist.lengthLinkedList())
linkedlist.removeData(8)
print("Size of linked list after deletion: ", linkedlist.lengthLinkedList())
print("Traversing linked list again: ")
linkedlist.traverse()