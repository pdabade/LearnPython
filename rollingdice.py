def rollingdice(input1,input2):
	num1 = {}
	num1 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
	num2 = {}
	num2 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
	if(len(input1) != len(input2)):
		return "Unlucky/Unlucky"
	for x in input1:
		for a,b in num1.iteritems():
			if x == a:
				num1[a] = b + 1
	for x in input2:
		for a,b in num2.iteritems():
			if x == a:
				num2[a] = b + 1
	print num1
	print num2
	if num1 != num2:
		return "Unlucky/Unlucky"
	else:
		return "Lucky/Lucky"
		
input1 = [12,5,6,5]
input2 = [5,5,6,12]

result = rollingdice(input1,input2)
print result
