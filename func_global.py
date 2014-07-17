x = 50
def func():
	global y
	print 'x is', y
	y = 2
	print 'Changed global x to', y

func()

print 'Value of x is', x
