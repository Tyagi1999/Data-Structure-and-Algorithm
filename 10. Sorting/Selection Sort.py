def SelectionSort(arr):
	for i in range(0, len(arr)-1):
		mini = i
		for j in range(i+1, len(arr)-1):
			if arr[j] < arr[mini]:
				mini = j
		if mini != i:
			swap(arr, mini, i)
	return arr
	
def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

if __name__ == "__main__":
	arr = [24, 12, -45, 78, 3, 1, 90, 5]
	print(SelectionSort(arr))
