def MergeSort(arr):
	if len(arr) == 1:
		return 
	middle = len(arr)//2
	lefthalf = arr[:middle]
	righthalf = arr[middle:]
	
	MergeSort(lefthalf)
	MergeSort(righthalf)
	
	i = 0
	j = 0
	k = 0
	
	while i < len(lefthalf) and j < len(righthalf):
		if lefthalf[i] < righthalf[j]:
			arr[k] = lefthalf[i]
			i+=1
		else:
			arr[k] = righthalf[j]
			j+=1
		k += 1
	while i < len(lefthalf):
		arr[k] = lefthalf[i]
		i+=1
		k+=1
	while j < len(righthalf):
		arr[k] = righthalf[j]
		j += 1
		k += 1

if __name__ == "__main__":
	arr = [2, 5, 1, -4, 3]
	MergeSort(arr)
	print(arr)