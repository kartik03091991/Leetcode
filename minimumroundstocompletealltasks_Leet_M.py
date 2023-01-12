from collections import Counter
#tasks = [2,2,3,3,2,4,4,4,4,4,7,7,7,7,7,7,7,7,7,7]
tasks = [2,3,3]

d1 = Counter(tasks)

print(d1)

taskcount = 0




for x in d1:
    if d1[x] % 3 == 0 and d1[x] != 1:
        print(d1[x],'1loop')
        a,b = divmod(d1[x],3)
        taskcount += a
        d1[x] = b
        print(a,b)

    elif d1[x] % 3 == 2 and d1[x] != 1:
        print(d1[x],'2loop')
        a,b = divmod(d1[x],3)
        print(a,b)
        taskcount += a + 1
        d1[x] -= (a*3) + 2
   
    elif d1[x] % 3 == 1 and d1[x] != 1:
        a,b = divmod(d1[x],3)
        print(a,b,'3loop')
        taskcount += (a-1) +2 
        d1[x] -= ((a-1)*3) + (2 *2)
    else:
        print(-1)

print(taskcount)
print(d1)



"""
Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.

"""