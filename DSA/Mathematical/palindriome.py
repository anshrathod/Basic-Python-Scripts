def palindrome(a):
	if str(a) == str(a)[::-1]:
		return True
	return False

if __name__ == "__main__":
	print(palindrome(12321))
	print(palindrome("wow"))
	print(palindrome(123123))
