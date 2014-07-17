number = 23
running = True
count = 0

while running:
	print '------------------------'
	guess = int(raw_input('Enter an integer: '))
	count += 1
	if guess == number:
		print 'You got it at attempt {0}!'.format(count)
		running = False
	elif guess < number:
		print 'Try higher numbers!'
	else:
		print 'Try lower numbers!'
else:
	print 'Exiting'
print 'Done...'
