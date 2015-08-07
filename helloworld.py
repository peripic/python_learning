#Ch5
print "hello world",   #Basic output in Python. Automatic new line, end with comma to avoid new line.

print 'hello python'   #Single quote - same as double quotes

print '''I asked, "What's his name?"'''   #Triple quotes can contain single & double quotes

#Escape sequence
print "What\'s your name?\n \"Lauren\", \tI answered.\\ "     #Backslash - same as C/C++/Java
print "First line. \
Second line"       #Use one backslash to indicate the string is continued in the next line. Otherwise wrong.
i = 6
print \
i   			#The same as print i
#Raw String
print r"Raw String - New lines are indicated by \n"
print r"What's your name? 'Lauren'\""    #Only single quote in double quotes, \" just show as \"
#format 5.4.5



##Ch6
#Operator
print 'a' + 'b'   	#ab
print 'a' * 3   	#aaa
print 3 ** 4		#81
print 3 <= 6		#True

#Expression
length = 5
breadth = 2
area = length * breadth
print "Area is", area	#pay attention to the print function
print "Perimeter is", 2 * (length + breadth)


















