def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    while B:
        if B[-1] > A[-1]:
            answer += 1
            A.pop()
        B.pop()
    return answer
