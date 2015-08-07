def say_hello():
	print 'Hello World!'


#parameter
def max(a, b):
	if a > b:
		print a, 'is max.'
	elif a == b:
		print a, 'is equal to', b
	else:
		print b, 'is max.'


#local and global
x = 50
def func_local(x):
	print 'x is', x
	x = 2
	print 'Changed local x to', x

func_local(x)
print 'x is still', x

def func_global():
	global x		#Use global to indicate this x is the same x outside the function
	print 'x is', x
	x = 2			#So here, global x is changed
	print 'Change global x to', x

func_global()
print 'x is now', x


#default value
def say(message, times=1):  #say(a, b=1) valid; say(a=1, b) not valid
	print message * times

say('Hello')    #1 time
say('World', 5) #5 times


#keyword arguments
def func(a, b=5, c=10):
	print 'a is', a, 'b is', b, 'c is', c

func(3, 7)   	#3, 7, 10
func(3, c=11) 	#3, 5, 11  here c=11 is keyword argument
func(c=12, a=4)	#4, 5, 12
	

#varargs arguments 8.6 to be read when encounter tuple and list


#return 
def max(a, b):
	'''Return the max one of the two parameters.   

	Input must be integers.'''		#The two lines are doc string! 
	if a > b:
		return a
	elif a == b:
		return 'Equal!' 	#Different types can be returned!!! Great!
	else:
		return b 			#return = return None, means return nothing

print max(5,5)
print max.__doc__		#Use .__**__ to retrive doc string

















