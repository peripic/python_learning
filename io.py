#Basic IO
def reverse(text):
	return text[::-1]

def is_palindorome(text):
	return text == reverse(text)

something = raw_input("Enter something:")	#raw_input receives the input from user 
if is_palindorome(something):
	print 'It is palindorome.'
else:
	print 'It is not palindorome.'




#File
poem = '''Life is short. 	
	Use Python!'''

f = open('poem.txt', 'w')	#Open a file with write mode
f.write(poem)
f.close()

f = open('poem.txt')	#Open a file with read mode. Default mode is txt and read
#Other modes: 't':text, 'b':binary, a':append, 'r':read
while True:
	line = f.readline()
	if len(line) == 0:	#If this line contains 0 chars, then EOF
		break;	
	print line,		#Why comma: readline() reads a whole line including the newline character at the end of a line
					#So use a comma to avoid additional newline
f.close()



#Pickle
import pickle

filename = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot', 'banana']

f = open(filename, 'wb')
pickle.dump(shoplist, f)	#Use pickle.dump() to store the list(object) into file
f.close()

del shoplist

f = open(filename, 'rb')
storedlist = pickle.load(f) #Use pickle.load() to retrive the list(object) from file
print '\n', storedlist
f.close()


class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

























