asia = set(['india','srilanka','malaysia','pakistan'])

country = 'india'

if country in asia:
	print country,' is in asia'
else:
	print country, ' is not in asia'

country = 'usa'

if country in asia:
	print country,' is in asia'
else:
	print country, ' is not in asia'


eurasia = asia.copy()
eurasia.add('russia')

if eurasia.issuperset(asia):
	print 'eurasia super set of asia'
	
print (asia & eurasia)
print (asia.union(eurasia))

