from math import sqrt
def U(n):
    if n< 0 :
        raise ValueError('invalid number')
    if n == 2 :
        return (1-sqrt(5))/2
    if n ==1 :
        return (1+sqrt(5))/2
    if n == 0 :
        return 3
    else:
        return U(n-1) *(-1)**n-((U(n-2))/(U(n-3)))