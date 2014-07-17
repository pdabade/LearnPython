import sys
import time

f = None
try:
	f = open('poem.txt')
	
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line,
		# flush to print to the screen immediately (?)
		sys.stdout.flush()
		print 'Press ctrl+c now'
		time.sleep(2)

except IOError:
	print 'Could not find the file'
except KeyboardInterrupt:
	print 'Reading from file cancelled.'
finally:
	if f:
		f.close()
	print 'Cleaning up: File closed'
