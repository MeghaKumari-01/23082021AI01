Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> ###### day 7
>>> 
>>> 
>>> ### 1
>>> 
>>> for i in range(5):
	print('*'*i)

	

*
**
***
****
>>> 
>>> ### 2
>>> 
>>> for i in range(5):
	print(' '*(4-i)+'*'*i)

	
    
   *
  **
 ***
****
>>> 
>>> ###3
>>> 
>>> for i in range(1,5):
	for j in range(1,i+1):
		print(j,end=' ')
	print(' ')

	
1  
1 2  
1 2 3  
1 2 3 4  
>>> 
>>> ###4
>>> 
>>> for i in range (1,5):
	for j in range (i):
		print(i)

		
1
2
2
3
3
3
4
4
4
4
>>> 
>>> for i in range (1,5):
	for j in range (i):
		print(i, end= ' ')
	print(' ')

	
1  
2 2  
3 3 3  
4 4 4 4  
>>> 
>>> ###5
>>> 
>>> for i in range (5):
	print('*'*i+' '*(8-(2*i))+'*'*i)

	
        
*      *
**    **
***  ***
********
>>> 
>>> 