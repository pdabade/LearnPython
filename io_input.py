def strip(text):
	t = text.upper()
	t = t.replace(" ","")
	t = t.translate(None,".,!'")
	return t
	
def is_palindrome(text):
	return strip(text) == strip(text[::-1])

go = True
while(go):
	something = raw_input('\nEnter "exit" to exit the program.\nEnter text: ')
	if something == 'exit':
		go = False
		print "Tata...!"
		break
	if is_palindrome(something):
		print "This is a palindrome."
	else:
		print "Not a palindrome."
