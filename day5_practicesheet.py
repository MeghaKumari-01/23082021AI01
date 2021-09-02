Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ###### day 5
>>> 
>>> ###2
>>> 
>>> 5**9
1953125
>>> 
>>> 3//2
1
>>> 
>>> 7//3
2
>>> 
>>> 7/3
2.3333333333333335
>>> 
>>> 6==6
True
>>> 
>>> a=20
>>> a+=3=
SyntaxError: invalid syntax
>>> a+=30
>>> print(a)
50
>>> a
50
>>> a%=3
>>> print(a)
2
>>> 
>>> True *False
0
>>> 
>>> True $ False
SyntaxError: invalid syntax
>>> True & False
False
>>> 
>>> True and False
False
>>> 
>>> True is False
False
>>> 
>>> False in 'False'
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
>>> 
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> 
>>> ((True == False) or (False >True)) and (False<=True)
False
>>> 
>>> ###3
>>> 
>>> s1='Nice to have it'
>>> s2='here'
>>> print(s1+' '+s2)
Nice to have it here
>>> 
>>> ###4
>>> 
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> print(a[3][1][2])
['hello']
>>> 
>>> ###5
>>> 
>>> a.insert(0,s1)
>>> a.insert(-1,s2)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 'here', 7]
>>> a.pop[-1]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.pop[-1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.pop(-1)
7
>>> a.pop(-1)
'here'
>>> a.insert(-1,s2)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 'here', 1]
>>> a.insert(7,s2)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 'here', 1, 'here']
>>> 
>>> ####6
>>> 
>>> n=[386,462,47,418,907,344,236,375,823,566,597,987,978,328,615,953,345,399,162,273,237,12,412,566,826,445,742,717]
>>> for i in n:
	while(i!=237):
		if(i%2==0):
			print(i)
		break
	else:
		break

	
386
462
418
344
236
566
978
328
162
>>> 
>>> ###7
>>> 
>>> cl_1= set(['white','black','red'])
>>> cl_2= set(['red','green'])
>>> print(cl_1.difference(cl_2))
{'black', 'white'}
>>> 
>>> ###8
>>> 
>>> s=input()
123045697840205506
>>> if(len(s)>=10):
	for i in range(10):
		if (str(i) not in s):
			print('not a pangram')
			break
		print('a pangram')
		break
else:
	print('not a pangram')

	
a pangram
>>> 
>>> ###9
>>> 
>>> n=int(input())
5
>>> print(n*(111+11+1))
615
>>> 
>>> 