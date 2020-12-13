class Stack():
	def __init__(self):
		self.stack = []
	
	def push(self, data):
		self.stack.append(data)
	
	def pop(self):
		removed_data = self.stack[-1]
		del self.stack[-1]
		return removed_data
	
	def peek(self):
		return self.stack[-1]
	
	def size(self):
		return len(self.stack)
	
	def traverseFromBottom(self):
		for i in self.stack:
			print(i, end = " ")
		print()
	
	def traverseFromTop(self):
		for i in range(len(self.stack)-1, -1, -1):
			print(self.stack[i], end = " ")
		print()
	
stack = Stack()
stack.push(10)
stack.push(12)
stack.push(15)
stack.push(20)
print("-----------------------------------")
print("Size of stack is: ", stack.size())
print("-----------------------------------")
print("Traversal from Bottom of stack: ")
stack.traverseFromBottom()
print("-----------------------------------")
print("Traversal from top of stack: ")
stack.traverseFromTop()
print("-----------------------------------")
stack.pop()
stack.pop()
print("Size of stack after pop operations: ", stack.size())
print("-----------------------------------")
print("Traversal from Bottom of stack: ")
stack.traverseFromBottom()
print("-----------------------------------")
print("Traversal from top of stack: ")
stack.traverseFromTop()