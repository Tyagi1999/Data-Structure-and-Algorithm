def InsertionSort(arr):
	for i in range(len(arr)):
		j = i
		while j > 0 and arr[j-1] > arr[j]:
			swap(arr, j, j-1)
			j -= 1
	return arr
	
def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

if __name__ == "__main__":
	arr = [-23, 4, -99, 2, 78, 34]
	print(InsertionSort(arr))