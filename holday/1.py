# s1 = 74
# s2 = 85
# r = (s2-s1)/s1 *100
# print(f"提升了{r:.2f}%")
from functools import reduce
from operator import xor


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(10)

def num( num):


    #num是一个数字把num拆开换成列表
    num = list(str(num))

