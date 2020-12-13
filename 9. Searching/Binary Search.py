def BinarySearch(arr, element):
	low = 0
	high = len(arr)-1
	while low <= high:
		mid = (low+high)//2
		if arr[mid] > element:
			high = mid-1
		elif arr[mid] < element:
			low = mid+1
		else:
			return mid
	return -1
	
if __name__ == "__main__":
	arr = [12, 45, 156, 7, 2, 89]
	element = 7
	arr.sort()   # Array needs to be sorted for Binary Search algorithm 
	res = BinarySearch(arr, element)
	if res == -1:
		print("Not found!!")
	else:
		print("Element found at index ", res)
			