Python 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 1.2.1      
>>> def findLine(x1,y1,x2,y2):
	m = float((y2-y1)/(x2-x1))
	m2 = x1*m
	b = y1/m2
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(10):
		print line1(element)
		ylist.append(line1(element))
		xlist.append(element)
	print xlist
	print ylist

	
>>> def makeLine(slope,intercept):
	def line(x):
           return slope * x + intercept
	return line

>>> 
>>> def findLine(x1,y1,x2,y2):
	m = float((y2-y1)/(x2-x1))
	m2 = x1*m
	b = y1/m2
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(10):
		print line1(element)
		ylist.append(line1(element))
		xlist.append(element)
	print xlist
	print ylist

	
>>> def findLine(x1,y1,x2,y2):
	import math
	m = float((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = x1*m
	b = y1/m2
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(line1(element))
		xlist.append(element)
	print xlist
	print ylist

	
>>> x = (10.310496704636941, -1.2028032151530954, 181.0)
>>> new = list(x)
>>> maximum = [new[0] +10,new[1]]
>>> minimum = [new[0]-10,new[1]]
>>> findLine(minimum[0],minimum[1],maximum[0],maximum[0])
1.07566499599
-3.60131034764
-3.60131034764
-2.52564535165
-1.44998035566
-0.374315359671
0.701349636319
1.77701463231
2.8526796283
3.92834462429
5.00400962028
6.07967461627
7.15533961226
8.23100460825
9.30666960423
10.3823346002
11.4579995962
12.5336645922
13.6093295882
14.6849945842
15.7606595802
16.8363245762
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[-3.6013103476394184, -2.5256453516499167, -1.4499803556604149, -0.37431535967091323, 0.70134963631858849, 1.7770146323080906, 2.8526796282975919, 3.9283446242870932, 5.0040096202765953, 6.0796746162660975, 7.1553396122555997, 8.2310046082451009, 9.3066696042346031, 10.382334600224105, 11.457999596213604, 12.533664592203106, 13.609329588192608, 14.68499458418211, 15.760659580171613, 16.836324576161115]
>>> def findLine(x1,y1,x2,y2):
	import math
	m = float((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = x1*m
	b = y1/m2
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> findLine(minimum[0],minimum[1],maximum[0],maximum[0])
1.07566499599
-3.60131034764
-3.60131034764
-2.52564535165
-1.44998035566
-0.374315359671
0.701349636319
1.77701463231
2.8526796283
3.92834462429
5.00400962028
6.07967461627
7.15533961226
8.23100460825
9.30666960423
10.3823346002
11.4579995962
12.5336645922
13.6093295882
14.6849945842
15.7606595802
16.8363245762
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[-3, -2, -1, 0, 0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
>>> x = (10.310496704636941, -1.2028032151530954, 181.0)
>>> list1 = list(x)
>>> truncated = [int(list1[0]),int(list1[1])]
>>> truncated
[10, -1]
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [new[0] +10,new[1]]minimum = [new[0]-10,new[1]]
	
SyntaxError: invalid syntax
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [new[0] +10,new[1]]minimum = [new[0]-10,new[1]]
	
SyntaxError: invalid syntax
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [list2[0] +10,list2[1]]
	minimum = [list2[0]-10,list2[1]]
	findLine(minimum[0],minimum[1],maximum[0],maximum[0])

	
>>> simplifier(x)

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    simplifier(x)
  File "<pyshell#29>", line 6, in simplifier
    findLine(minimum[0],minimum[1],maximum[0],maximum[0])
  File "<pyshell#14>", line 6, in findLine
    b = y1/m2
ZeroDivisionError: float division
>>> simplifier((10.310496704636941, -1.2028032151530954, 181.0))

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    simplifier((10.310496704636941, -1.2028032151530954, 181.0))
  File "<pyshell#29>", line 6, in simplifier
    findLine(minimum[0],minimum[1],maximum[0],maximum[0])
  File "<pyshell#14>", line 6, in findLine
    b = y1/m2
ZeroDivisionError: float division
>>> def findLine(x1,y1,x2,y2):
	import math
	m = float((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = x1*m
	b = int(y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [list2[0] +10,list2[1]]
	minimum = [list2[0]-10,list2[1]]
	findLine(minimum[0],minimum[1],maximum[0],maximum[0])

	
>>> simplifier((10.310496704636941, -1.2028032151530954, 181.0))

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    simplifier((10.310496704636941, -1.2028032151530954, 181.0))
  File "<pyshell#35>", line 6, in simplifier
    findLine(minimum[0],minimum[1],maximum[0],maximum[0])
  File "<pyshell#33>", line 6, in findLine
    b = int(y1/m2)
ZeroDivisionError: float division
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [list2[0] +10,list2[1]]
	minimum = [list2[0]-10,list2[1]]
	print maximum
	print minimum

	
>>> simplifier((10.310496704636941, -1.2028032151530954, 181.0))
[20, -1]
[0, -1]
>>> def findLine(x1,y1,x2,y2):
	import math
	m = float((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = x1*m
	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> b = -1/1.0
>>> b
-1.0
>>> def findLine(x1,y1,x2,y2):
	import math
	m = ((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = x1*m
	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [list2[0] +10,list2[1]]
	minimum = [list2[0]-10,list2[1]]
	findLine(minimum[0],minimum[1],maximum[0],maximum[0])

	
>>> simplifier((10.310496704636941, -1.2028032151530954, 181.0))

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    simplifier((10.310496704636941, -1.2028032151530954, 181.0))
  File "<pyshell#49>", line 6, in simplifier
    findLine(minimum[0],minimum[1],maximum[0],maximum[0])
  File "<pyshell#47>", line 6, in findLine
    b = (y1/m2)
ZeroDivisionError: integer division or modulo by zero
>>> def findLine(x1,y1,x2,y2):
	import math
	m = int((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = x1*m
	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [list2[0] +10,list2[1]]
	minimum = [list2[0]-10,list2[1]]
	findLine(minimum[0],minimum[1],maximum[0],maximum[0])

	
>>> simplifier((10.310496704636941, -1.2028032151530954, 181.0))

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    simplifier((10.310496704636941, -1.2028032151530954, 181.0))
  File "<pyshell#54>", line 6, in simplifier
    findLine(minimum[0],minimum[1],maximum[0],maximum[0])
  File "<pyshell#52>", line 6, in findLine
    b = (y1/m2)
ZeroDivisionError: integer division or modulo by zero
>>> def findLine(x1,y1,x2,y2):
	import math
	m = ((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = x1*m
	b = float(y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [list2[0] +10,list2[1]]
	minimum = [list2[0]-10,list2[1]]
	findLine(minimum[0],minimum[1],maximum[0],maximum[0])

	
>>> simplifier((10.310496704636941, -1.2028032151530954, 181.0))

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    simplifier((10.310496704636941, -1.2028032151530954, 181.0))
  File "<pyshell#59>", line 6, in simplifier
    findLine(minimum[0],minimum[1],maximum[0],maximum[0])
  File "<pyshell#57>", line 6, in findLine
    b = float(y1/m2)
ZeroDivisionError: integer division or modulo by zero
>>> def findLine(x1,y1,x2,y2):
	import math
	m = ((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = float(x1*m)
	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> simplifier((10.310496704636941, -1.2028032151530954, 181.0))

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    simplifier((10.310496704636941, -1.2028032151530954, 181.0))
  File "<pyshell#59>", line 6, in simplifier
    findLine(minimum[0],minimum[1],maximum[0],maximum[0])
  File "<pyshell#62>", line 6, in findLine
    b = (y1/m2)
ZeroDivisionError: float division
>>> def findLine(x1,y1,x2,y2):
	import math
	from __future__ import division
	m = ((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = float(x1*m)
	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist
	
SyntaxError: from __future__ imports must occur at the beginning of the file
>>> 
>>> from __future__ import division
>>> 
>>> def findLine(x1,y1,x2,y2):
	import math
	from __future__ import division
	m = ((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = float(x1*m)
	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist
	
SyntaxError: from __future__ imports must occur at the beginning of the file
>>> def findLine(x1,y1,x2,y2):
	import math
	m = ((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = (x1*m)
	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [list2[0] +10,list2[1]]
	minimum = [list2[0]-10,list2[1]]
	findLine(minimum[0],minimum[1],maximum[0],maximum[0])

	
>>> simplifier((10.310496704636941, -1.2028032151530954, 181.0))

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    simplifier((10.310496704636941, -1.2028032151530954, 181.0))
  File "<pyshell#72>", line 6, in simplifier
    findLine(minimum[0],minimum[1],maximum[0],maximum[0])
  File "<pyshell#70>", line 6, in findLine
    b = (y1/m2)
ZeroDivisionError: float division
>>> def findLine(x1,y1,x2,y2):
	import math
	m = ((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = (x1*m)
	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> def findLine(x1,y1,x2,y2):
	import math
	m = ((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = (x1*m)
	if m2 is 0:
		m2+1
	
	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist

	
>>> def simplifier(point):
	list1 = list(x)
	list2 = [int(list1[0]),int(list1[1])]
	maximum = [list2[0] +10,list2[1]]
	minimum = [list2[0]-10,list2[1]]
	findLine(minimum[0],minimum[1],maximum[0],maximum[0])

	
>>> simplifier((10.310496704636941, -1.2028032151530954, 181.0))

Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    simplifier((10.310496704636941, -1.2028032151530954, 181.0))
  File "<pyshell#79>", line 6, in simplifier
    findLine(minimum[0],minimum[1],maximum[0],maximum[0])
  File "<pyshell#77>", line 9, in findLine
    b = (y1/m2)
ZeroDivisionError: float division
>>> def findLine(x1,y1,x2,y2):
	import math
	m = ((y2-y1)/(x2-x1))
	xdifference = math.fabs(x2-x1)
	m2 = (x1*m)
	if m2 is 0:
		m2+1

	b = (y1/m2)
	print m
	print b
	ylist = []
	xlist = []
	line1 = makeLine(m,b)
	for element in range(int(xdifference)):
		print line1(element)
		ylist.append(int(line1(element)))
		xlist.append(element)
	print xlist
	print ylist
