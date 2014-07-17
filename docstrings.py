def print_max(x,y):
	'''Prints the max of 2 numbers.
	
	The two values must be integers.'''
	
	#convert to int if possible
	x = int(x)
	y = int(y)
	
	if x > y:
		print x, ' is maximum'
	else:
		print y, ' is maximum'
		
print_max(3,5)
print print_max.__doc__

#docstrings: a multi-line string where the first line starts with a capital letter and ends with a dot.
# Then the second line is blank followed by any detailed explanation starting from third line.
