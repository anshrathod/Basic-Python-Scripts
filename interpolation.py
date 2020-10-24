#Interpolation search algorithm
def interpolationSearch(A, x):

	# search space is A[left..right]
	(left, right) = (0, len(A) - 1)

	while A[right] != A[left] and A[left] <= x <= A[right]:

		# estimate mid
		mid = left + (x - A[left]) * (right - left) // (A[right] - A[left])

		# key value is found
		if x == A[mid]:
			return mid

		# discard all elements in the right search space
		# including the mid element
		elif x < A[mid]:
			right = mid - 1

		# discard all elements in the left search space
		# including the mid element
		else:
			left = mid + 1

	# if key is found
	if x == A[left]:
		return left

	# x doesn't exist in the list
	return -1


if __name__ == '__main__':

	A = [2, 5, 6, 8, 9, 10]
	key = 5

	index = interpolationSearch(A, key)

	if index != -1:
		print("Element found at index", index)
	else:
		print("Element found not in the list")
