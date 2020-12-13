class HashTable():
	def __init__(self):
		self.size = 10
		self.keys = [None]*self.size
		self.values = [None]*self.size
		
	def put(self, key, data):
		index = self.hashfunction(key)
		while self.keys[index] is not None:
			if self.keys[index] == key:
				self.values[index] = data
				return 
			index = (index + 1)%self.size
		self.keys[index] = key
		self.values[index] = data
	
	def get(self, key):
		index = self.hashfunction(key)
		while self.keys[index] is not None:
			if self.keys[index] == key:
				return self.values[index]
			index = (index + 1)%self.size
		return None
	
	def hashfunction(self, key):
		sum = 0
		for pos in range(len(key)):
			sum += ord(key[pos])
		return sum%self.size
	
if __name__ == "__main__":
	table = HashTable()
	table.put("Clay", 98)
	table.put("Tony", 85)
	table.put("Shroud", 90)
	table.put("Toni", 80)
	
	print(table.get("Justin"))
	print(table.get("Tony"))
	
	print("Key table is: ", table.keys)
	print("Values table is: ", table.values)