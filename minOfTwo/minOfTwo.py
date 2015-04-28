# create an empty list
inputList = []

# open the file containing the input
with open('input.txt') as f:
	for line in f:
		for word in line.split():
			# add elements to the empty list
			inputList.append(word)

# remove the first or 0th element of the list 
# and store it in a variable
n = inputList.pop(0)

# start finding the min of two numbers at a time
while inputList:
	x = inputList.pop(0)
	y = inputList.pop(0)
	print min(int(x), int(y))