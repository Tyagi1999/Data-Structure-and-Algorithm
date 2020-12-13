class Node():
	def __init__(self, character):
		self.character = character
		self.left = None
		self.right = None
		self.middle = None
		self.value = 0
		
class TST():
	def __init__(self):
		self.root = None
	
	def put(self, key, value):
		self.root = self.putItem(self.root, key, value, 0)
		
	def putItem(self, node, key, value, index):
		c = key[index]
		if node == None:
			node = Node(c)
		if c < node.character:
			node.left = self.putItem(node.left, key, value, index)
		elif c > node.character:
			node.right = self.putItem(node.right, key, value, index)
		elif index < len(key)-1:
			node.middle = self.putItem(node.middle, key, value, index+1)
		else:
			node.value = value
		return node
	
	def get(self, key):
		node = self.getItem(self.root, key, 0)
		if node == None:
			return -1
		return node.value
	
	def getItem(self, node, key, index):
		if node == None:
			return None
		c = key[index]
		if c < node.character:
			return self.getItem(node.left, key, index)
		elif c > node.character:
			return self.getItem(node.right, key, index)
		elif index < len(key)-1:
			return self.getItem(node.middle, key, index+1)
		else:
			return node

if __name__ == "__main__":
	tst = TST()
	tst.put("apple", 100)
	tst.put("mango", 200)
	tst.put("man", 300)
	
	print(tst.get("mango"))
	print(tst.get("man"))
	print(tst.get("adam"))