#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
n = 3

print( int(round(1/5**0.5 * (((1+5**0.5)/2.0)**(n+1) - ((1-5**0.5)/2.0)**(n+1)))))

print((1+5**0.5))
print(((1+5**0.5)/2.0))
print(((1+5**0.5)/2.0)**(n+1))
print(((1-5**0.5)/2.0)**(n+1))

print(round((((1+5**0.5)/2.0)**(n+1) - ((1-5**0.5)/2.0)**(n+1))))


from math import factorial
def climbStairs(self, n):
    res= 0
    two = n//2

    for i in range(two+1):
        t = i           # number of twos
        o = n-t*2       # number of ones
        res += factorial(t+o)/(factorial(t)*factorial(o))     # (two+one)!/ (two!*one!)
            
    return res

    