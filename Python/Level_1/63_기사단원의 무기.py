def solution(number, limit, power):
    li = [0]*(number+1)
    for i in range(1,number+1):
        for j in range(i,number+1,i):
            li[j] += 1

    for i in range(number + 1):
        if li[i] > limit:
            li[i] = power
    return sum(li)