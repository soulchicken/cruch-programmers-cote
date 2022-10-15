def solution(n):
    answer = 0
    for i in range(1,n+1):
        while 1:
            answer += 1
            if answer % 3 and '3' not in str(answer):
                break
    return answer