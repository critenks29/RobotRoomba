Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import time
>>> import create

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import create
  File "C:\Python27\lib\create.py", line 18, in <module>
    import serial
ImportError: No module named serial
>>> #To use this file, all you have to do is import this file in PythonWin.
"""Here are the full instructions actually:
1) Turn on the robot
2) Plug the robot USB into your laptop
3) Run PythonWin
4) Press CTRL + i
5) Choose this file

And everything should work automatically
"""
import time
import create
r = create.Create(3)

'Here are the full instructions actually:\n1) Turn on the robot\n2) Plug the robot USB into your laptop\n3) Run PythonWin\n4) Press CTRL + i\n5) Choose this file\n\nAnd everything should work automatically\n'
>>> r.move(40,0)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    r.move(40,0)
NameError: name 'r' is not defined
>>>  def makeLine(slope,intercept):

        def line(x):
            return slope * x + intercept

        return line
  File "<pyshell#4>", line 1
    def makeLine(slope,intercept):
   ^
IndentationError: unexpected indent
>>>  def makeLine(slope,intercept):
	def line(x):
            return slope * x + intercept
	return line
  File "<pyshell#5>", line 1
    def makeLine(slope,intercept):
   ^
IndentationError: unexpected indent
>>> 
>>> def makeLine(slope,intercept):
	def line(x):
           return slope * x + intercept
	return line

>>> line1 = makeLine(5,-3)
>>> line1
<function line at 0x0242F9F0>
>>> print line1
<function line at 0x0242F9F0>
>>> line1(9)
42
>>> line1(50)
247
>>> line1(1)
2
>>> def findLine(x1,y1,x2,y2):
	m = (y2-y1)/(x2,x1)
	m2 = x1*m
	b = y1/m2
	return m
	return b

>>> findLine(1,1,5,6)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    findLine(1,1,5,6)
  File "<pyshell#21>", line 2, in findLine
    m = (y2-y1)/(x2,x1)
TypeError: unsupported operand type(s) for /: 'int' and 'tuple'
>>> def findLine(x1,y1,x2,y2):
	m = (y2-y1)/(x2-x1)
	m2 = x1*m
	b = y1/m2
	return m
	return b

>>> findLine(1,1,5,6)
1
>>> def findLine(x1,y1,x2,y2):
	m = (y2-y1)/(x2-x1)
	m2 = x1*m
	b = y1/m2
	print m
	print b

	
>>> findLine(1,1,5,6)
1
1
>>> def findLine(x1,y1,x2,y2):
	m = float((y2-y1)/(x2-x1))
	m2 = x1*m
	b = y1/m2
	print m
	print b

	
>>> findLine(1,1,5,6)
1.0
1.0
>>> findLine(1.0,1.0,5.0,6.0)
1.25
0.8
>>> 
>>> 



>>> 

>>> 


>>> 


>>> 


>>> 


>>> 

>>> 



>>> 

>>> 



>>> 


>>> 


>>> 


>>> 


>>> 


>>> 

>>> 



>>> 


>>> 

>>> 



>>> 

>>> 



>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 

>>> 



>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 



>>> 


>>> 

>>> 



>>> 

>>> 



>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 



>>> 

>>> 



>>> 


>>> 


>>> 



>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 

>>> 


>>> 



>>> 

>>> 



>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 


>>> 

>>>  findLine(1.0,1.0,5.0,6.0)
 
  File "<pyshell#135>", line 1
    findLine(1.0,1.0,5.0,6.0)
   ^
IndentationError: unexpected indent
>>> 
>>> findLine(1.0,1.0,5.0,6.0)
1.25
0.8
>>> def findLine(x1,y1,x2,y2):
	m = float((y2-y1)/(x2-x1))
	m2 = x1*m
	b = y1/m2
	print m
	print b
	line1 = makeLine(m,b)
	for element in range(10):
		print line1(element)

		
>>> findLine(1.0,1.0,5.0,6.0)
1.25
0.8
0.8
2.05
3.3
4.55
5.8
7.05
8.3
9.55
10.8
12.05
>>> def findLine(x1,y1,x2,y2):
	m = float((y2-y1)/(x2-x1))
	m2 = x1*m
	b = y1/m2
	print m
	print b
	line1 = makeLine(m,b)
	for element in range(10):
		print line1(element)

		
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

	
>>> findLine(1.0,1.0,5.0,6.0)
1.25
0.8
0.8
2.05
3.3
4.55
5.8
7.05
8.3
9.55
10.8
12.05
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0.8, 2.05, 3.3, 4.55, 5.8, 7.05, 8.3, 9.55, 10.8, 12.05]
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
	print 'xlist:' xlist
	print 'ylist:' ylist
	
SyntaxError: invalid syntax
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

	
>>> findLine(1.0,1.0,5.0,6.0)
1.25
0.8
0.8
2.05
3.3
4.55
5.8
7.05
8.3
9.55
10.8
12.05
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0.8, 2.05, 3.3, 4.55, 5.8, 7.05, 8.3, 9.55, 10.8, 12.05]
>>> x = (10.310496704636941, -1.2028032151530954, 181.0)
>>> new = list(x)
>>> new
[10.310496704636941, -1.2028032151530954, 181.0]
>>> minimum = new
>>> maximum = [new[0] +10]
>>> maximum
[20.31049670463694]
>>> maximum = [new[0] +10,new[1]]
>>> maximum
[20.31049670463694, -1.2028032151530954]
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
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[-3.6013103476394184, -2.5256453516499167, -1.449980355660415, -0.37431535967091323, 0.7013496363185885, 1.7770146323080906, 2.852679628297592, 3.928344624287093, 5.004009620276595, 6.0796746162660975]
>>> 
