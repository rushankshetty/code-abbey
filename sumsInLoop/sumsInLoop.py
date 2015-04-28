from __future__ import print_function

# create an empty list
inputList = []
outputList = []

# open the file containing the input
with open('input.txt') as f:
	for line in f:
		for word in line.split():
			# add elements to the empty list
			inputList.append(word)

# remove the first or 0th element of the list 
# and store it in a variable
n = inputList.pop(0)

# start adding two numbers at a time
while inputList:
	x = inputList.pop()
	y = inputList.pop()
	outputList.append(int(x) + int(y))

# reverse the list
outputList.reverse()

# print the output
print(*outputList, sep = ' ')