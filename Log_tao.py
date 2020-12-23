Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Turtle()
>>> tao.shape('turtle')
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.forward(100)
>>> tao.left(90)
>>> tao.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x000001F98553ECA0>>
>>> tao.reset()
>>> for i in range(4)
SyntaxError: invalid syntax
>>> for i in range(4):
	tao.forward(100)tao.left(90)
	
SyntaxError: invalid syntax
>>> for i in range(4):
	tao.forward(100)
	tao.left(90)

	
>>> range (4)
range(0, 4)
>>> list (range(4))
[0, 1, 2, 3]
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
\
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range[10,50,90]:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    for i in range[10,50,90]:
TypeError: 'type' object is not subscriptable
>>> for i in[10,50,90]:
	print(i)

	
10
50
90
>>> range (1,10)
range(1, 10)
>>> list (range(1,10))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> tao.reset()
>>> for i in range (4):
	tao.forward(100)
	tao.left(90)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
>>> tao.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x000001F98553ECA0>>
>>> tao.reset()
>>> tao.forward(100)
>>> tao.left(45)
>>> tao.forward(100)
>>> tao.left(45)
>>> tao.forward(100)
>>> tao.left(45)
>>> tao.forward(100)
>>> tao.left(45)
>>> tao.forward(100)
>>> tao.left(45)
>>> tao.forward(100)
>>> tao.left(45)
>>> tao.forward(100)
>>> tao.left(45)
>>> tao.forward(100)
>>> for i in range (8):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> tao.reset()
>>> for i in range (8):
	tao.forward(100)
	tao.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> tao.reset()
>>> def regtangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

		
>>> regtangle()
>>> tao.reset()
>>> for i in range(10):
	regtangle()
	tao.left(36)

	
>>> tao.reset()
>>> 