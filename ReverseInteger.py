rawInput = str(input("Enter a number and reverse it: "))

def ReverseInteger(raw):
	rawRev = [raw[x] for x in range(len(raw))]

	if rawRev[0] == "-":
		data = rawRev[1::]
		newData = [data[-index-1] for index in range(len(data))]

		for x in range(len(newData)):
			if newData[x] == "0":
				newData[x] = ""

		newData = "".join(newData)
		return f"-{newData}"

	else:
		data = rawRev[0::]
		newData = [data[-index-1] for index in range(len(data))]

		for x in range(len(newData)):
			if newData[x] == "0":
				newData[x] = ""

		return "".join(newData)



print(ReverseInteger(rawInput))