#words = ["abc","deq","mee","aqq","dkd","ccc"] 
words = 'abc'
pattern = "abb"

d1 = {}


x = zip(words,pattern)

#print(x)

for y in x:
    print(y)

m1 = {}
m2 = {}

for w,p in zip(words,pattern):
    if w not  in m1:
        m1[w] = p
    if p not in m2:
        m2[p] = w
    print(m1, 'm1')
    print(m2,'m2')
    print(m1[w],m2[p] ,p,w)
    if (m1[w],m2[p]) != (p,w):
        print(False)
    


#final solution
""" 

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)

"""