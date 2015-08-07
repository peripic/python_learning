import sys
import os

print 'Command line arguments are:'
for i in sys.argv:			#sys.argv returns a list of command line arguments(list of string). File name is arg0
	print i

print '\n\n Python running path:', sys.path    #Use sys.path to get the 
print '\n\n Current working directory:', os.getcwd()   #return current working directory


from math import sqrt			#Not suggest to use
print 'The squre root of 16:', sqrt(16), '\n\n'


#Import self-defined module
import mymodule 		
mymodule.say_hi() 	
print 'Mymodule version:', mymodule.__version__

from mymodule import say_hi, __version__		#another way to import
say_hi()
print 'Mymodule version:', __version__

#if use: from mymodule import *, can only import say_hi(), cannot import __version
#And avoid using from...import *  !!!


#Use dir() to list all identifiers in a module

#Arrange modules in a folder. Every folder containing modules should include a init.py file


