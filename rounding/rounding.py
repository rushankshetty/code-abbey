#!/usr/bin/env python 

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

# convert the string list into float list
inputList = map(float, inputList)

# start the divison of two numbers 
while inputList:
	x = inputList.pop(0)
	y = inputList.pop(0)
	# round-off the result and then truncate the decimal part
	# as round() returns a float value 
	print int(round(x / y))
