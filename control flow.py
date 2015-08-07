
# number = 23 
# guess = int(raw_input('Enter an integer:'))

# if guess == number:			#Pay attention to the colon!
# 	print 'You guessed it!'
# elif guess < number:
# 	print 'A little lower!'
# else:
# 	print 'A little higher!'

# print 'Done!'

# no switch statement in Python
# command + / to comment a block in sublime

#while loop & if statement
number = 23
running = True

while running:
	guess = int(raw_input('Enter an integer:'))   #input is string, convert to int

	if guess == number:			
		print 'You guessed it!'
		running = False  	#change to break => else statement will not execute
	elif guess < number:
		print 'A little lower!'
	else:
		print 'A little higher!'
else:			#The else statement after while is executed the first time loop condition is false.
	print 'The while loop is done!'   	#But it will not execute if use break to end loop!!!!




#for loop
for i in range(1,5):  #iterate over a sequence of objects
	print i
else:			#same as while's else. not execute if break
	print 'For loop is done!'
#range(): generate a sequence [1,2,3,4], the second number not included.
#1 step by default; range(1,5,2) step is 2 => [1,3]
#range() output one number per time. list(range(1,5)) to get [1,2,3,4]




#break and continue
while True:
	s = raw_input('Enter something:')
	if s == 'quit':
		break
	elif len(s) < 3:		#len() to get the length of a string
		print 'Too small'
		continue
	print 'Sufficient length!'
















