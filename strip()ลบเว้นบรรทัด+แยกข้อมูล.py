Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#######################################
>>> print('hello world')
hello world
>>> 
>>> print('hello world\n')
hello world

>>> print('hello world\n'.strip())
hello world

#######################################
car = ['toyota','isuzu','honda']
print (car[0])
toyota
car = ['toyota','isuzu','honda']
print (car[1])
isuzu
car = ['toyota','isuzu','honda']
print (-2)
-2
print (car[-2])
isuzu

#############################
result = ['hh,jj,ll,2023-09-21 23:22:53 \n',' yy,uu,ii,2023-09-21 23:23:01']
>>> for r in result:
...     print(r.strip())
... 
...     
hh,jj,ll,2023-09-21 23:22:53
yy,uu,ii,2023-09-21 23:23:01
>>> 
>>> for r in result:
...     print(r.strip().split(','))
... 
...     
['hh', 'jj', 'll', '2023-09-21 23:22:53']
['yy', 'uu', 'ii', '2023-09-21 23:23:01']

>>> 
>>> t = 'yy,uu,ii,2023-09-21 23:23:01'
>>> t.split(',')
['yy', 'uu', 'ii', '2023-09-21 23:23:01']
