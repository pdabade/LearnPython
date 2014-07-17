print 'Simple Assignment'
shoplist = ['aa', 'bb', 'cc', 'dd']
print shoplist

mylist = shoplist

del shoplist[0]

print 'shoplist : ', shoplist
print 'mylist : ', mylist

print '\nCopy by making a full slice'
shoplist = ['aa', 'bb', 'cc', 'dd']
print shoplist

mylist = shoplist[:]

del shoplist[0]

print 'shoplist : ', shoplist
print 'mylist : ', mylist
