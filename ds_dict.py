# Dictionary like address book
# key value pairs
# keys are immutable objects - like strings
# values can be mutable or immutable

ab = {'Pooja':'Dabade','Ganga':'Koli','Kshitij':'Joshi'}

print 'Pooja surname is : ', ab['Pooja']
print ab

print "Deleting Ganga's entry..."

ganga = ab['Ganga']

print ganga

del ab['Ganga']

print ab
print 'Adding Jugal...'
ab['Jugal'] = 'Parikh'

for val in ab:
	print val, ' -> ', ab[val]

if 'Ganga' in ab:
	print ab['Ganga']
else:
	ab['Ganga'] = 'Koli'
	
for name, address in ab.items():
	print 'Firstname: {}, Lastname: {}'.format(name,address)
