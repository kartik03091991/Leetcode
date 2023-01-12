#word = "USA"
#word = "leetcode"
word = "Google"

if word.isupper():
    print(True)
elif word.islower():
    print(True)
elif word[0].isupper() and word[1:].islower():
    print(True)
else:
    print(False)



