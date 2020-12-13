def QuickSort(arr, low, high):
	if low >= high:
		return 
	pivot = partition(arr, low, high)
	QuickSort(arr, low, pivot-1)
	QuickSort(arr, pivot+1, high)
	
def partition(arr, low, high):
	pivot = (low+high)//2
	swap(arr, pivot, high)
	i = low
	for j in range(low, high):
		if arr[j] <= arr[high]:
			swap(arr, i, j)
			i += 1
	swap(arr, i, high)
	return i

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

if __name__ == "__main__":
	arr = [-4, -2, 1, 56, 2, -65, 78]
	QuickSort(arr, 0, len(arr)-1)
	print(arr)