# My shopping list
shoplist = ["apple", "corns", "carrot", "chocolates"]

print 'I have ', len(shoplist), ' items to purchase'

print 'The items are: '
for n in shoplist:
	print n

print '\nI also have to buy figs.'
shoplist.append('figs')

print 'My shopping list now: ', shoplist

print 'Sorted list:'
shoplist.sort()
print shoplist

print 'Deleting 1st item.'
olditem = shoplist[0]
del shoplist[0]

print shoplist
print 'Bought ',olditem
