import sys
import os
from math import sqrt
import mymodule

print 'The command line arguments are: '
argv = "Pooja"
print argv

for i in sys.argv:
	print i
	
print '\n\nThe PYTHONPATH is ',sys.path, '\n'

print os.getcwd()

print 'Square root of 16 is: ', sqrt(16)

if __name__ == '__main__':
	print 'This program is being run by itself'

print sqrt.__name__

mymodule.sayHello("Pooja")
print 'Version: ', mymodule.__version__

print dir('mymodule')
