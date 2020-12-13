class Heap():
	MAX_SIZE = 10
	def __init__(self):
		self.heap = [0]*Heap.MAX_SIZE
		self.currentPosition = -1
	
	def insert(self, item):
		if self.isFull():
			print("Heap is full!!!")
			return 
		self.currentPosition += 1
		self.heap[self.currentPosition] = item
		self.fixUp(self.currentPosition)
	
	def isFull(self):
		if self.currentPosition == Heap.MAX_SIZE:
			return True
		else:
			return False
	
	def fixUp(self, index):
		parentIndex = int((index-1)/2)
		while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
			temp = self.heap[index]
			self.heap[index] = self.heap[parentIndex]
			self.heap[parentIndex] = temp
			parentIndex = int((index-1)/2)
	
	def heapSort(self):
		for i in range(0, self.currentPosition+1):
			temp = self.heap[0]
			print("%d" %temp)
			self.heap[0] = self.heap[self.currentPosition-i]
			self.heap[self.currentPosition-i] = temp
			self.fixDown(0, self.currentPosition - i - 1)
		
	def fixDown(self, index, upto):
		while index <= upto:
			left = 2*index + 1
			right = 2*index + 2
			
			if left < upto:
				childToSwap = None
				if right > upto:
					childToSwap = left
				else:
					if self.heap[left] > self.heap[right]:
						childToSwap = left
					else:
						childToSwap = right
				if self.heap[index] < self.heap[childToSwap]:
					temp = self.heap[index]
					self.heap[index] = self.heap[childToSwap]
					self.heap[childToSwap] = temp
				else:
					break
				index = childToSwap
			else:
				break
	
if __name__ == "__main__":
	heap = Heap()
	heap.insert(10)
	heap.insert(-20)
	heap.insert(0)
	heap.insert(2)
	
	heap.heapSort()
					