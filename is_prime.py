""" function to test is number is primea numbers """
from math import sqrt
def func_prime(x):
    if x < 2 :
        return False
    for i in range(2,int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True
    