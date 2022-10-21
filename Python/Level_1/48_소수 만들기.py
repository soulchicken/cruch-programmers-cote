def solution(nums):
    n = [1]*3001
    for i in range(2,3001):
        if n[i]:
            for j in range(i*2,3001,i):n[j]=0
    answer = 0
    from itertools import combinations as c
    for x,y,z in c(nums, 3):
        if n[x + y + z]: answer += 1
    return answer