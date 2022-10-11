def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(2,i):
            if not i%j:
                answer +=1
                break
    return answer