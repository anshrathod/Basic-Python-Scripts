# import string module to use ascii_lowercase
import string

# define alphabet variable to use ascii_lowercase
alphabet = string.ascii_lowercase

# define encryption function
def encrypt(text, shift):
	# define empty string to store encrypted text
	encrypted_text = ""
	# loop through each character in text
	for char in text:
		# if character is not in alphabet, add to encrypted_text
		if char not in alphabet:
			encrypted_text += char
		# else, add shifted character to encrypted_text
		else:
			encrypted_text += alphabet[(alphabet.index(char) + shift) % 26]
	# return encrypted_text
	return encrypted_text

# define decryption function
def decrypt(text, shift):
	# define empty string to store decrypted text
	decrypted_text = ""
	# loop through each character in text
	for char in text:
		# if character is not in alphabet, add to decrypted_text
		if char not in alphabet:
			decrypted_text += char
		# else, add shifted character to decrypted_text
		else:
			decrypted_text += alphabet[(alphabet.index(char) - shift) % 26]
	# return decrypted_text
	return decrypted_text

# define main function
def main():
	# define text variable
	plain_text = input("Enter Some Text: ")
	# define shift variable
	key = int(input("Enter Key: "))
	# call encrypt function with text and shift variables
	encrypted_text = encrypt(plain_text, key)
	# print encrypted_text
	print(encrypted_text)
	# call decrypt function with encrypted_text and shift variables
	decrypted_text = decrypt(encrypted_text, key)
	# print decrypted_text
	print(decrypted_text)

# call main function
main()
