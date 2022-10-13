def solution(n):
    answer = []
    while n != 1:
        for i in range(2,n+1):
            if not n%i:
                n //= i
                if i not in answer:
                    answer.append(i)
                break
    return answer