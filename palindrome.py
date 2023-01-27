
data = str(input("Enter a text: ")).lower()
data = "".join(data.split())
x = "".join([data[index] for index in range(len(data))])
xRev = "".join([x[-(index+1)] for index in range(len(x))])

if (x ==  xRev):
	print("Your text is a palindrome!")
else:
	print("Try again, that was not correct!")