# create an empty list
inputList = []

# open the file containing the input
with open('input.txt') as f:
	for line in f:
		for word in line.split():
			# add elements to the empty list
			inputList.append(word)

# print the output
print "Sum of two numbers is: ", sum(int (i) for i in inputList)