import random
import math
lst1 = []
lst2 = []
size = int(input('size lst1 = '))
for i in range(size):
    temp = int(input('=> '))
    lst1.append(temp)

size = int(input('size lst1 = '))
for i in range(size):
    temp = int(input('=> '))
    lst1.append(temp)

for i in lst1:
    if i % 2 != 0:
        lst2.append(i)
print(lst2)
