def solution(n):
    answer = 0
    while n:
        answer += answer*2 + n % 3
        n //= 3
    return answer