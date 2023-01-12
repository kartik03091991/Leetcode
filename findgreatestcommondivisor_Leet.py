#nums = [2,5,6,9,10]
#nums = [7,5,6,8,3]
nums = [3,3]

mina = min(nums)
maxa = max(nums)

print(mina,maxa)


lstmincommon = []

for x in range(1,mina+1):
    if mina % x == 0:
        lstmincommon.append(x)

lstmaxcommon = []

for x in range(1,maxa+1):
    if maxa % x == 0:
        lstmaxcommon.append(x)

print(lstmincommon)
print(lstmaxcommon)

common = []

for x in lstmincommon:
    if x in lstmaxcommon:
        common.append(x)

print(common)
print(max(common))