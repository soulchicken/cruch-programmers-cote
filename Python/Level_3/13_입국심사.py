def solution(n, times):
    left = 0
    right = n * min(times)
    answer = right
    while left < right:
        mid = (left + right) // 2
        total = 0
        for time in times:
            total += mid // time
        if total >= n:
            if answer > mid:
                answer = mid
            right = mid
        else:
            left = mid + 1
    return answer
