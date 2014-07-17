def return_LowestHighest(list):
	min = list[0]
	max = list[0]
	for num in list:
		if num<min:
			min = num
		if num>max:
			max = num
	return (min,max)
	
list = [3,6,2,8,9,7,1,0,4,5]
min, max = return_LowestHighest(list)

print 'Minimum: {0}  Maximum: {1}'.format(min,max)
