from queue import Queue

#n = 2

q = Queue()

print(q)

q.put('1')
print(q)


n = 63 
lst1 = []

while n > 0:
    n -= 1
    s1 = q.get()
    print(s1)
    lst1.append(s1)
    s2 = s1
    q.put(s1 + "0")

    q.put(s2 + "1")


print(lst1)

lst2 = []

for x in range(0,len(lst1)):
    lst2.append(int(lst1[x]))

print(lst2)


s = "82734"

slen = len(s)

# 1 digit = 1
# 2 digit = 3 (1 + 2)
# 3 digit = 7 (1 + 2 + 4 )
# 4 digit = 15 (1+ 2 + 4 + 8 )
# 5 digit = 31 ( 1 + 2 + 4 + 8 + 16)
# 6 digit = 63 ( 1 + 2 + 4 + 8 + 16 + 32)
