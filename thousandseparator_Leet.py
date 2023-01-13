#n = 12345678925627
#n = 123456789
#n = 1234
#n = 987
n = 0
#n = 51040

print(divmod(n,1000))
print(round(n/1000),3)

#print(2**31)

lst1 = []

s1 = str(n)


for x in range(-1,-len(s1)-1,-1):
    #print(x)
        if x % (-3) == 0:
            #print(s1[x])
            lst1.insert(0,s1[x])
            lst1.insert(0,'.')
        else:
            lst1.insert(0,s1[x])


#lst1.reverse()

print(lst1)
print("".join(lst1))

if len(s1) <=  3:
    print(s1)
else:
    if lst1[0] == '.':
        print("".join(lst1[1:])) 
    else:
        print("".join(lst1))


"""

for x in range(0,6):
    q,r  = divmod(n,1000)
    print(q,r)
    lst1.insert(0,str(r))
    n = q
    print(n,q)
    if n == 0:
        break


print(lst1)
print(".".join(lst1))
"""

"""
Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
"""