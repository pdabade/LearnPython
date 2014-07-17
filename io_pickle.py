import pickle

shoplistfile = 'shoplist.data'

shoplist = ['litchie','guava','blueberries','mango']

f = open(shoplistfile,'wb')
pickle.dump(shoplist,f)
f.close()

del shoplist

f = open(shoplistfile,'rb')
list = pickle.load(f)
print list
f.close()
