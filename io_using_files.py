poem = '''This is a poem.. 
Ha ha..
Wah wah...'''

f = open('poem.txt','w')
f.write(poem)
f.close()

#read is the default mode of opening a file
f = open('poem.txt')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line,
	
f.close()
