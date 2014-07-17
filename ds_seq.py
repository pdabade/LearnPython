shoplist = ['apple', 'mango', 'fig', 'berry', 'orange']
name = 'aaraadhyaa'

# indexing or subscription

print 'Item 0 : ',shoplist[0]
print 'Item 1 : ',shoplist[1]
print 'Item 2 : ',shoplist[2]
print 'Item 3 : ',shoplist[3]
print 'Item -1 : ',shoplist[-1]
print 'Item -2 : ',shoplist[-2]

print 'Character 0:',name[0]

#Slicing on a list

print 'Item 1 - 3 : ',shoplist[1:3]
print 'Item 1 - -1 : ',shoplist[1:-1]
print 'Item start to end : ',shoplist[:]

#Slicing on string

print 'Character 1 - 5 : ',name[1:5]
print 'Character 1 - -7 : ',name[1:-7]
print 'Character start to end : ',name[:]

#step operator

print shoplist[::2]
