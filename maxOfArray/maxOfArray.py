# create an empty list
inputList = []

# open the file containing the input
with open('input.txt') as f:
	for line in f:
		for word in line.split():
			# add elements to the empty list
			inputList.append(word)

# convert the string list into integer list
inputList = map(int, inputList)

# find the max in the array
print max(inputList)

# find the min in the array
print min(inputList)

