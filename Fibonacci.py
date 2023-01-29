nums = [1, 1]

def FibonacciSequence(limit):
	for index in range(2, limit):
		newNum = nums[index-2] + nums[index-1]
		nums.append(newNum)

FibonacciSequence(20)
print(nums)