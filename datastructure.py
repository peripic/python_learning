#List
shoplist = ['apple', 'mango', 'carrot', 'banana']  #Definition of a list

print 'I have', len(shoplist), 'to buy.'	#Use len() to get the number of items in the list
print 'They are:'

for item in shoplist:
	print item,		#Use a comma to print in a line

print '\nI also need to buy rice.'
shoplist.append('rice')		#Add an item in a list, can add any type. append(5) is ok
print 'My shoplist is now:', shoplist	#Print a list

print 'I will sort my shoplist now.'
shoplist.sort()				#Sort a list, list is mutable, so sort will change the list directly instead of returning a new list.
print 'My shoplist is now:', shoplist		#String is immutable

print 'I am going to buy the first item:', shoplist[0]
del shoplist[0]			#Delete the first item in the list
print 'My shoplist is now:', shoplist

anotherlist = ['bowl', 'plate']
shoplist.extend(anotherlist)    #add another list to the old list, use extend
print 'add two new items', shoplist



#Tuple
zoo = ('python', 'elephant', 'penguin')
print '\n\nThe old zoo has', len(zoo), 'animals.'
print 'They are',
for animal in zoo:
	print animal,

new_zoo = 'monkey', 'camel', zoo	#parentheses are optional
print '\nNumber of cages in the new zoo is', len(new_zoo)   #3
print 'All animals in new zoo are', new_zoo		
#('monkey', 'camel', ('python', 'elephant', 'penguin'))  A tuple in a tuple does not lose its identity!!!
print 'Animals brought from old zoo are', new_zoo[2]	#So here new_zoo[2] gets the old zoo tuple (zoo is the 3rd item in new_zoo)
print 'Last animal brought from old zoo is', new_zoo[2][2]	#Here new_zoo[2][2] gets the 3rd item in the old zoo
print 'Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2])

#Tuple with only 1 item:
#sigle = (2, ) to defer from sigle = (2) just 2 with parentheses




#Dictionary
ab = {
	'yumo' : 'yumo@yale.edu',
	'yuanyuan' : 'yuanyuan@yale.edu',
	'luyang' : 'luyang@yale.edu'
}

print "\n\nyumo's address is", ab['yumo']   	#Use indexing operator to get the value of a key
del ab['luyang']	#Delete a key-value pair

print 'There are', len(ab), 'contacts in the address book.'		#Use len() to get the number of pairs
print 'They are:'
for name, add in ab.items():	#How to iterate the dictionay - Use items()
	print 'Contact', name, 'at', add

ab['cat'] = 'cat.luyang@yale.edu'	#Add an item to the dictionary
if 'cat' in ab:		#Use "in" to check whether a key is in the dictionary or not
	print 'Cat is in the address book at', ab['cat']




#Sequence: string, list, tuple
#Features:
#1. membership test: "in" / "not in" expressions
#2. indexing operation
#3. slicing operation

shopList = ['apple', 'mango', 'carrot', 'banana']
name = 'yuanyuanzhang'
#Indexing operation
print '\n\nItem 0 is', shopList[0]	#apple
print 'Item 1 is', shopList[1]	#mango
print 'Item -1 is', shopList[-1]	#banana
print 'Item -2 is', shopList[-2]	#carrot
print 'Character 0 is', name[0]		#y

#Slicing on a list: first included, second excluded, starting from 0
print 'Item [0, 3) is', shopList[0 : 3]  		#apple, mango, carrot
print 'Item 2 to the end is', shopList[2 : ]	#carrot, banana
print 'Item 1 to -1 is', shopList[1 : -1] 		#mango, carrot
print 'All items', shopList[:]	#all

#Same as string

#Add step for slicing
print '\nStep is 1', shopList[::1]  	#0,1,2,3
print 'Step is 2', shopList[::2]	#0,2
print 'Step is 3', shopList[::3]	#0,3
print 'Step is -1', shopList[::-1]	#-1,-2,-3,-4




#Set
coutries = set(['india', 'us', 'canada'])
print '\n\n','india' in coutries	#True
print 'uk' in coutries		#False
cc = coutries.copy()
cc.add('china')	
print cc.issuperset(coutries)	#True
coutries.remove('us')
print coutries & cc    #india, canada



#Reference - True copy using a full slice
myList = shopList 	#myList is just another name pointing to the same object!
del myList[0]		
print 'shopList:', shopList
print 'myList', myList		#Should be the same

myList = shopList[:]	#Make a full slice copy to myList, myList is another object!
del myList[0]
print 'shopList:', shopList
print 'myList', myList		#Not same



















