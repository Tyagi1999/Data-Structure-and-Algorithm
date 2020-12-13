def LinearSearch(arr, element):
	for i in arr:
		if i == element:
			return "Found the element"
	return "Element not found"

if __name__ == "__main__":
	arr = [12, 24, 5, 3, 78, 2]
	element = 78
	print(LinearSearch(arr, element))