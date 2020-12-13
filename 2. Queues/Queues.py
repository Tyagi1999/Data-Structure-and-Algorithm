class Queue():
	def __init__(self):
		self.queue = []
	
	def enqueue(self, data):
		self.queue.append(data)
	
	def dequeue(self):
		removed_data = self.queue[0]
		del self.queue[0]
		return removed_data
	
	def size(self):
		return len(self.queue)
	
	def peek(self):
		return self.queue[0]
	
	def traversal(self):
		for i in self.queue:
			print(i)
	
queue = Queue()
queue.enqueue(2)
queue.enqueue(10)
queue.enqueue(4)
queue.enqueue(15)
queue.enqueue(9)

print("Size of Queue is: ", queue.size())
print("------------------------------------")
print("Traversal is: ")
queue.traversal()
print("------------------------------------")

queue.dequeue()
queue.dequeue()

print("Size of Queue after removing elements is: ", queue.size())
print("------------------------------------")
print("Traversal is: ")
queue.traversal()