def solution(array, n):
    answer = 0
    gap = 200
    for i in sorted(array):
        if abs(n-i) < gap: answer,gap = i,abs(n-i)
    return answer