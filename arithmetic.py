import math

def sum(a,b):
    c=a+b
    return c

def diff(a,b):
    c=a-b
    return c
    
def mul(a,b):
    c=a*b
    return c
    
def div(a,b):
    c=a/b
    return c

def isPrime(n):
    if n<=1:
        return false
    if n==2:
        return true
    if n%2==0:
        return false
    for t in range(3,int(math.sqrt(n)+1),2):
        if n%t==0:
            return false
    return true
    for n in range(30):
        return isPrime(n)
            