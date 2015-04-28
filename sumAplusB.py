inputList = []

with open('example.txt') as f:
	for line in f:
		for word in line.split():
			inputList.append(word)

print "Sum of two numbers is: ", sum(int (i) for i in inputList)