def total(initial=5, *numbers, **keywords):
	count = initial
	for num in numbers:
		count += num
	for key in keywords:
		count += keywords[key]
	return count
	
print total(10,vegetables=50, fruits=20)

# when a *param is declared, all the positional args from that point till end are collected a a tuple called param
# when **param is declared, all the args are collected as a dictionary called param
