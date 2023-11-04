Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cars = ['toyota','honda','benz']
cars.append('byd')
print(cars)
['toyota', 'honda', 'benz', 'byd']
['toyota', 'honda', 'benz', 'byd']
['toyota', 'honda', 'benz', 'byd']
cars.remove('honda')
print(cars)
['toyota', 'benz', 'byd']
cars.insert(0,'tesla')
print(cars)
['tesla', 'toyota', 'benz', 'byd']
print(cars[0])
tesla
print(cars[1])
toyota
for c in cars:
    print(c)

    
tesla
toyota
benz
byd
print(*cars)
tesla toyota benz byd
for i,c in enumerate(cars):
    print(i,c)

    
0 tesla
1 toyota
2 benz
3 byd
for i,c in enumerate(cars, start=0):
    print('ลำดับที่ {} {} '.format(i,c))

    
ลำดับที่ 0 tesla 
ลำดับที่ 1 toyota 
ลำดับที่ 2 benz 
ลำดับที่ 3 byd 
for i,c in enumerate(cars, start=1):
    print('ลำดับที่ {} {} '.format(i,c))

    
ลำดับที่ 1 tesla 
ลำดับที่ 2 toyota 
ลำดับที่ 3 benz 
ลำดับที่ 4 byd 
print(cars)
['tesla', 'toyota', 'benz', 'byd']
for c in cars:
    print(c)

    
tesla
toyota
benz
byd
i = 0
>>> for c in cars:
...     print(i+1, c)
...     i = i +1
... 
...     
1 tesla
2 toyota
3 benz
4 byd
>>> #modify car
>>> 4 byd
SyntaxError: incomplete input
>>> print(cars)
['tesla', 'toyota', 'benz', 'byd']
>>> #modify car
>>> cars[1]= 'isuzu'
>>> print(cars)
['tesla', 'isuzu', 'benz', 'byd']
>>> del cars[2]
>>> print(cars)
['tesla', 'isuzu', 'byd']
>>> len(cars)
3
>>> ord('ก')
3585
>>> ord('ข')
3586
>>> for i in range(3585,3595):
...     print(chr(i))
... 
...     
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
