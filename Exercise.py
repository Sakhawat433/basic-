from random import randint
L1 = [randint(1,100) for i in range(50)]
print(L1)
L2 =[i**2 for i in L1]
print(L2)
count= len([i for i in L2 if i>50])
print(count)
from random import choice
alphabet = 'abcdefghijklmnopqrstuvwxyz'
s1 = ''.join([choice(alphabet) for i in range(1000)])
print(s1)
s2 = ' '.join([choice(alphabet) for i in range(1000)])
print(s2)
