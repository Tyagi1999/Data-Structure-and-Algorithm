def CountingSort(A):
	K = max(A)
	B = [0 for el in A]
	C = [0 for el in range(0, K+1)]
	
	for i in range(0, K+1):
		C[i] = 0
	
	for j in range(0, len(A)):
		C[A[j]] += 1
	
	for i in range(1, K+1):
		C[i] += C[i-1]
	
	for j in range(len(A)-1, -1, -1):
		tmp = A[j]
		tmp2 = C[tmp] - 1
		B[tmp2] = tmp
		C[tmp] -= 1
	
	return B
	
if __name__ == "__main__":
	A = [234, 21, 45, 12, 78, 3, 672]
	print("Sorted array is : {}".format(CountingSort(A)))