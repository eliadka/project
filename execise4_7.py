from itertools import count
from math import factorial
#################
def fibo_gen(num):
    i = 1
    while i <= num:
        i += 1
        yield i

q = 1
my_fifteen = []
for el in fibo_gen(5):
    if q > 15:
        break
    else:
        my_fifteen.append(el)
        q +=1
print(my_fifteen)
