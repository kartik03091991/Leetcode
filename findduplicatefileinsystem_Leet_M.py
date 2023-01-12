paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
#Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]


lstdirectory = []
lstfiles = []



for x in paths:
    a = x.split(' ')
    print(a)
    lstdirectory.append(a[0])
    lstfiles.append

print(lstdirectory)


"""
for x in paths:
    for y in range(0,len(x)):
        if x[y] == ' ' :
            #lstspace.append(y)
            lstdirectory.append(x[:y])
            #print(lstdirectory)
            break

print(lstdirectory)

filelist = []

for x in paths:
    for y in range(0,len(x)):
        if x[y] == ' ':
            filelist.append(x[y+1:])
            #print(filelist)
            break
print(filelist)

"""