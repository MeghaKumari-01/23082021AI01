Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:/Users/Aniket/Desktop/megha/day8_task.py =============
not my string
>>> 
================================ RESTART: Shell ================================
>>> ###### all occurence are same
>>> s='wweerrttyy'
>>> s1={i:s.count(i)for i in s}
>>> d=set(s1.values())
>>> if len(d)==1:
	print('my string')
elif len(d)==2:
	x=list(s1.values())
	x1={j:x.count(j) for j in x}
	y=list(x1.values())
	z=list(x1.keys())
	if 1 in y:
		if int(z[y.index(1)])-1 ==int(z[1-y.index(1)]):
			print('my string')
		else:
			print('not my string')
	else:
		print('not my string')
else:
	print('not my string')

	
my string
>>> 
>>> 
>>> ###### one occurence is one more
>>> s='wweerrttyyy'
>>> s1={i:s.count(i)for i in s}
>>> d=set(s1.values())
>>> if len(d)==1:
	print('my string')
elif len(d)==2:
	x=list(s1.values())
	x1={j:x.count(j) for j in x}
	y=list(x1.values())
	z=list(x1.keys())
	if 1 in y:
		if int(z[y.index(1)])-1 ==int(z[1-y.index(1)]):
			print('my string')
		else:
			print('not my string')
	else:
		print('not my string')
else:
	print('not my string')

	
my string
>>> 
>>> 
>>> ###### one occurence is one less
>>> 
>>> s='wweerrtty'
>>> s1={i:s.count(i)for i in s}
>>> d=set(s1.values())
>>> if len(d)==1:
	print('my string')
elif len(d)==2:
	x=list(s1.values())
	x1={j:x.count(j) for j in x}
	y=list(x1.values())
	z=list(x1.keys())
	if 1 in y:
		if int(z[y.index(1)])-1 ==int(z[1-y.index(1)]):
			print('my string')
		else:
			print('not my string')
	else:
		print('not my string')
else:
	print('not my string')

	
not my string
>>> 
>>> ######## different occurences
>>> 
>>> s='wweerrttytbnv'
>>> s1={i:s.count(i)for i in s}
>>> d=set(s1.values())
>>> if len(d)==1:
	print('my string')
elif len(d)==2:
	x=list(s1.values())
	x1={j:x.count(j) for j in x}
	y=list(x1.values())
	z=list(x1.keys())
	if 1 in y:
		if int(z[y.index(1)])-1 ==int(z[1-y.index(1)]):
			print('my string')
		else:
			print('not my string')
	else:
		print('not my string')
else:
	print('not my string')

	
not my string
>>> 
>>> 