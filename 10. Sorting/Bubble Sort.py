def BubbleSort(arr):
	for i in range(0, len(arr)-1):
		for j in range(0, len(arr)-1-i):
			if arr[j] > arr[j+1]:
				swap(arr, j, j+1)
	return arr
	
def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

if __name__ == "__main__":
	arr = [2, 6, -1, 5, -30, 7, 4, 90, 9]
	print(BubbleSort(arr))
	