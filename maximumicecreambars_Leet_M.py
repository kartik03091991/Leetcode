costs = [1,3,2,4,1] 
coins = 7

#costs = [10,6,8,7,7,8] 
#coins = 5

#costs = [1,6,3,1,2,5]
#coins = 20


costs.sort()
print(costs)
count1 = 0

if sum(costs) <= coins:
    print(len(costs))
elif costs[0] > coins:
    print(0)
else:
    for x in costs:
        if x <= coins:
            coins -= x
            count1 += 1

    print(count1)


"""
Example 1:

Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
Example 2:

Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.
Example 3:

Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
"""