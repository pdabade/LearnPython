try:
	text = raw_input('Enter something --> ')
except EOFError:
	print 'Why EOF?'
except KeyboardInterrupt:
	print 'Cancelled operation'
else:
	print 'Entered: {}'.format(text)
