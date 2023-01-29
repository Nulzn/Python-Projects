import random
import math

while True:
	a = math.pow(random.randint(1, 100), 2)
	b = math.pow(random.randint(1, 100), 2)

	if (a + b) == 1000 and a < b and b < 1000:
		print(f"Found | A: {math.sqrt(a)} B: {math.sqrt(b)}")
		break
	else:
		print("Not Found!")