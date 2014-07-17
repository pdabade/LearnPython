def say(msg, times=1):
	print msg * times
	
say("Hello")
say("Pooja", 3)

def func(a, b=5, c=10):
	print "a = {0}, b = {1}, c = {2}.".format(a,b,c)

func(0)
func(1,2)
func(1,2,3)
