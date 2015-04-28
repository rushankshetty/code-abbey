inputList = []

with open('example.txt') as f:
	for line in f:
		for word in line.split():
			inputList.append(word)

n = inputList.pop(0)

print "The sum of", n, "values is:", sum(int (i) for i in inputList)