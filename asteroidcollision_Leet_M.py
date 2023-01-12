#asteroids = [5,10,-5]
#asteroids = [8,-8]
asteroids = [10,2,-5]
#asteroids = [10,-5]
#asteroids = [-2,-1,1,2]
# make asteroids = lstcount1
lstcount1 = []
p = 5
count2 = 0
count3 = 0

while count3 < 3:
    lstcount1.clear()
    for x in range(0,len(asteroids)):
        print(x,'x')
        for y in asteroids[x+1:]:
            if asteroids[x] > 0 and y < 0:  # + - (right left smaller one is destroyed)
                print(asteroids[x] , y, 'line1')
                if abs(asteroids[x]) > abs(y):
                    lstcount1.append(asteroids[x]) 
                elif abs(asteroids[x]) < abs(y):
                    lstcount1.append(y)
                else:
                    pass
            elif asteroids[x] < 0 and y > 0: # - + left right none is destroyed 
                lstcount1.append(asteroids[x])
                lstcount1.append(y)
            elif asteroids[x] < 0 and y < 0:                            # -- ,++ none is destroyed 
                lstcount1.append(asteroids[x])
                #lstcount1.append(y)
            else:
                lstcount1.append(y)
            count2 += 1
            print(lstcount1, 'lstcount1 line2')
            print(asteroids,'asteroids')
            if count2 == 1:
                break
        count2 = 0
    if len(lstcount1) == len(asteroids):
        break   
    asteroids.clear()
    for i in range(0,len(lstcount1)):
        asteroids.append(lstcount1[i])

    
        #count2 = 0
    count3 += 1

print(lstcount1)