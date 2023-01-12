
#defining input for sample

ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2


#Computing the area of first rectangle a

#print(ax1, ay1)
length_a = abs(ax1) + abs(ax2)
breadth_a = abs(ay1) + abs(ay2)

area_a =  length_a * breadth_a

#Computing the area of second rectangle b

#print(bx1, by1)
length_b = abs(bx1) + abs(bx2)
breadth_b = abs(by1) + abs(by2)

area_b =  length_b * breadth_b


print(area_a ,area_b)

#putting all coordinates of ax in list

lst_ax = []

count1 = 0
while count1 <= length_a:
    lst_ax.append(ax1)
    ax1 += 1
    count1 += 1

print(lst_ax)


#putting all coordinates of bx in list

lst_bx = []

count2 = 0
while count2 <= length_b:
    lst_bx.append(bx1)
    bx1 += 1
    count2 += 1

print(lst_bx)
    

# Finding the length of common area lst_ax and lst_bx

set_ax = set(lst_ax)
set_bx = set(lst_bx)
set_cx = set_ax.intersection(set_bx)
length_cx =  len(set_cx)-1 
print(length_cx)

#putting all coordinates of ay in list

lst_ay = []

count3 = 0
while count3 <= breadth_a:
    lst_ay.append(ay1)
    ay1 += 1
    count3 += 1

print(lst_ay)


#putting all coordinates of by in list

lst_by = []

count4 = 0
while count4 <= breadth_b:
    lst_by.append(by1)
    by1 += 1
    count4 += 1

print(lst_by)

    

# Finding the breadth of common area lst_ay and lst_by

set_ay = set(lst_ay)
set_by = set(lst_by)
set_cy = set_ay.intersection(set_by)
breadth_cy =  len(set_cy)-1 

print(breadth_cy)

# area of common rectangle

area_common = length_cx *  breadth_cy
print(area_common)

# subtracting the common area from the area covered by two rectangles
final_result = area_a + area_b - area_common

print(final_result)