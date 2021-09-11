Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ####10
>>> 
>>> v=input().split('#')
23 89 6#87 9 12
>>> x=[int(i) for i in x.split()]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x=[int(i) for i in x.split()]
NameError: name 'x' is not defined
>>> v=input()
23 89 6#87 9 12
>>> x,y=v.split('#')
>>> x=[int(i) for i in x.split()]
>>> y=[int(i) for i in y.split()]
>>> print(x,y)
[23, 89, 6] [87, 9, 12]
>>> 
>>> 
>>> ###11
>>> 
>>> v= input().split(',')
v.sort()
>>> print(','.join(v))
v.sort()
>>> 
>>> v= input().split(',')
bag,me,without,zebra
>>> v.sort()
>>> print(','.join(v))
bag,me,without,zebra
>>> 
>>> 
>>> ###12
>>> 
>>> d={}
>>> d={ 'student':['rahul','kishore','vidya'],
    'marks': ['54','87','98']
    }
>>> d['student'][d['marks'].index(max(d['marks']))]
'vidya'
>>> 
>>> 
>>> ###13
>>> 
>>> s=input()
hello world! 1234
>>> x=[i for i in s if isalpha(i)]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x=[i for i in s if isalpha(i)]
  File "<pyshell#34>", line 1, in <listcomp>
    x=[i for i in s if isalpha(i)]
NameError: name 'isalpha' is not defined
>>> help(isalpha)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    help(isalpha)
NameError: name 'isalpha' is not defined
>>> x=[i for i in s if i.isalpha()]
>>> y=[i for i in s if i.isnum()]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    y=[i for i in s if i.isnum()]
  File "<pyshell#37>", line 1, in <listcomp>
    y=[i for i in s if i.isnum()]
AttributeError: 'str' object has no attribute 'isnum'
>>> y=[i for i in s if i.isnumeric()]
>>> print('digits:'len(y)'  letters:'len(x))
SyntaxError: invalid syntax
>>> print(len(y))
4
>>> print(len (x))
10
>>> print('digits:'len(y))
SyntaxError: invalid syntax
>>> 
>>> 
>>> ####15
>>> 
>>> n=input()
70
>>> l= [ i for i in range(n+1) if not(i%7)
     print(l)
     
SyntaxError: invalid syntax
>>> l= [ i for i in range(n+1) if not(i%7)]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    l= [ i for i in range(n+1) if not(i%7)]
TypeError: can only concatenate str (not "int") to str
>>> int n=input()
SyntaxError: invalid syntax
>>> n=int(input())
70
>>> l= [ i for i in range(n+1) if not(i%7)]
>>> print(l)
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
>>> 
>>> 
>>> 
>>> ####14
>>> 
>>> d={'name': ['akash','sonia','visakha']'
   
SyntaxError: EOL while scanning string literal
>>> d={'name': ['akash','sonia','visakha'],
   'subject':['python','java','python'],
   'ratings':[8.4,7.8,8]
   }
>>> n=input()
python
>>> ind={list(d.keys()).index(i) if i==n for i in d['subject'] }
SyntaxError: invalid syntax
>>> ind={list(d.keys()).index(i) if i==n else print('not found') for i in d['subject'] }
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    ind={list(d.keys()).index(i) if i==n else print('not found') for i in d['subject'] }
  File "<pyshell#67>", line 1, in <setcomp>
    ind={list(d.keys()).index(i) if i==n else print('not found') for i in d['subject'] }
ValueError: 'python' is not in list
>>> ind={d.keys().index(i) if i==n else print('not found') for i in d['subject'] }
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    ind={d.keys().index(i) if i==n else print('not found') for i in d['subject'] }
  File "<pyshell#68>", line 1, in <setcomp>
    ind={d.keys().index(i) if i==n else print('not found') for i in d['subject'] }
AttributeError: 'dict_keys' object has no attribute 'index'
>>> ind={list(d.keys())[1].index(i) if i==n else print('not found') for i in d['subject'] }
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    ind={list(d.keys())[1].index(i) if i==n else print('not found') for i in d['subject'] }
  File "<pyshell#69>", line 1, in <setcomp>
    ind={list(d.keys())[1].index(i) if i==n else print('not found') for i in d['subject'] }
ValueError: substring not found
>>> ind={list(d[subject]).index(i) if i==n else print('not found') for i in d['subject'] }
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    ind={list(d[subject]).index(i) if i==n else print('not found') for i in d['subject'] }
  File "<pyshell#70>", line 1, in <setcomp>
    ind={list(d[subject]).index(i) if i==n else print('not found') for i in d['subject'] }
NameError: name 'subject' is not defined
>>> ind={list(d['subject']).index(i) if i==n else print('not found') for i in d['subject'] }
not found
>>> 
>>> 
>>> ind={list(d['subject']).index(i) if i==n  for i in d['subject'] }
SyntaxError: invalid syntax
>>> ind=[]
>>> for i in d['subject']:
	if i==n:
		
SyntaxError: multiple statements found while compiling a single statement
>>> ind=[]
>>> 
SyntaxError: multiple statements found while compiling a single statement
>>> ind=[]
>>> 
>>> for i in d['subject']:
	if i==n:
		
SyntaxError: invalid syntax
>>> ind=[]
>>> for i in d['subject']:
	if i==n:
		ind+=list(d['subject']).index(i)

		
Traceback (most recent call last):
  File "<pyshell#84>", line 3, in <module>
    ind+=list(d['subject']).index(i)
TypeError: 'int' object is not iterable
>>> for i in d['subject']:
	if i==n:
		ind+=d['subject'].index(i)

		
Traceback (most recent call last):
  File "<pyshell#86>", line 3, in <module>
    ind+=d['subject'].index(i)
TypeError: 'int' object is not iterable
>>> for i in d['subject']:
	if i==n:
		ind+=d['subject'].index(n)

		
Traceback (most recent call last):
  File "<pyshell#88>", line 3, in <module>
    ind+=d['subject'].index(n)
TypeError: 'int' object is not iterable
>>> for i in d['subject']:
	if i==n:
		ind+ d['subject'].index(n)

		
Traceback (most recent call last):
  File "<pyshell#90>", line 3, in <module>
    ind+ d['subject'].index(n)
TypeError: can only concatenate list (not "int") to list
>>> for i in d['subject']:
	if i==n:
		ind+ list(d['subject'].index(n))

		
Traceback (most recent call last):
  File "<pyshell#92>", line 3, in <module>
    ind+ list(d['subject'].index(n))
TypeError: 'int' object is not iterable
>>> for i in d['subject']:
	if i==n:
		ind+=list(d['subject'].index(n))

		
Traceback (most recent call last):
  File "<pyshell#94>", line 3, in <module>
    ind+=list(d['subject'].index(n))
TypeError: 'int' object is not iterable
>>> for i in d['subject']:
	if i==n:





for i in d['subject']:
	if i==n:
		ind+=list(d['subject'].index(n))
		
SyntaxError: expected an indented block
>>> 
>>> for i in d['subject']:
	if i==n:
		print(list(d['subject'].index(n)))

		
Traceback (most recent call last):
  File "<pyshell#103>", line 3, in <module>
    print(list(d['subject'].index(n)))
TypeError: 'int' object is not iterable
>>> for i in d['subject']:
	if i==n:
		print(d['subject'].index(n))

		
0
0
>>> print
<built-in function print>
>>> 90
90
>>> print(d['subjects'])
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    print(d['subjects'])
KeyError: 'subjects'
>>> print(d['subject'])
['python', 'java', 'python']
>>> print(d['subject'].index('python'))
0
>>> for i in d['subject']:
		print(d['subject'].index(n))

		
0
0
0
>>> for i in d['subject']:
		print(d['subject'].index(i))

		
0
1
0
>>> 