class ShortInputException(Exception): 	#Create a exception class inherited from Exception
	"""A user defined Exception here."""
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length		#It has two fields.
		self.atleast = atleast

try:
	text = raw_input('Enter something:') 	
	if len(text) < 3:
		raise ShortInputException(len(text), 3)		#Raise an exception with arguments
except EOFError:
	print 'Why did you do an EOF on me?'
except ShortInputException as ex: 	#Catch the exception and store as variable ex
	print 'ShortInputException: The input was:', ex.length, \
	'expected at least:', ex.atleast 		#Get the fields using indexing operator
else:
	print 'No exception raised!'



#################
#try...finally
import sys
import time

f = None
try:
	f = open("poem.txt")			#Typical reading a file
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line,
		sys.stdout.flush()		#Use flush() to output the line immediately
		print "Press Ctr + C now!"
		time.sleep(2)			#Wait for 2 seconds to wait for the input
except IOError:
	print "Could not find the file!"
except KeyboardInterrupt:
	print "You cancelled the reading from file!"
finally:						#"finally" clause will always execute
	if f:
		f.close()				#So the file will be closed even if the KeyboardInterrupt has been raised!
	print "File has been closed!"




















