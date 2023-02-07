def solution(n, stations, w):
    answer = 0
    i = 0
    W = 2*w + 1
    for j in stations:
        if i < j - w - 1:
            gap = j - w - i - 1
            answer += (gap // W)
            if gap % W:
                answer += 1
        i = j + w
    if i < n:
        gap = n - i
        answer += (gap // W)
        if gap % W:
            answer += 1
    return answer
