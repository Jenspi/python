# October 30, 2019 // Jennifer Spicer
password = input("Enter a password to check if valid: ")

min_length = 5
max_length = 10
special_chars = ["@", "%", "+", "\\", "/", "'", "!", "#", "$", "^", "?", ":", ".", "(", ")", "{", "}", "[", "]", "~", "`", "-", "_", ".", "&", "\""] #must contain at least one of these
illegal_chars = [" "] #not valid if password contains these

def valid_length(password):
	length=len(password)
	if len(password)>=min_length and len(password)<=max_length:
		return True
	else:
		print("Password length needs to be 5-10 characters long. Your password is "+str(length)+" characters long.")
		return False

def valid_case(password):
	uppercase = False
	for char in password:
		if char.isupper():
			uppercase = True
	return uppercase

def valid_chars(password):
	spaces = False
	special = False
	number = False

	for char in password:
		for i in illegal_chars:
			if char == i:
				spaces = True
		for s in special_chars:
			if char == s:
				special = True
		if char.isdigit():
			number = True

	if spaces==False and special==True and number==True:
		return True
	else:
		print("Included special character(s): "+str(special))
		print("Included at least one number: "+str(number))
		print("Included NO SPACES: "+ str(not spaces))
		return False

print("⋆ ˚｡⋆୨୧˚　˚୨୧⋆｡˚ ⋆⋆ ˚｡⋆୨୧˚　˚୨୧⋆｡˚ ⋆⋆ ˚｡⋆୨୧˚　˚୨୧⋆｡˚ ⋆⋆ ˚｡⋆୨୧˚　˚୨୧⋆｡˚ ⋆")
if valid_length(password) and valid_chars(password) and valid_case(password):
	print("✓ Valid password")
else:
	print("✗ Invalid password")