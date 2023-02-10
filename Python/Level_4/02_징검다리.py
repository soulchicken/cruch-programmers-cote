def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.sort()
    while left <= right:
        mid = (left + right) // 2
        count = 0
        idx = mid
        for rock in rocks:
            if rock < idx:
                count += 1
            else:
                idx = rock + mid
        if distance < idx:
            count += 1
        if count > n:
            right = mid - 1
        else:
            left = mid + 1
    return (left + right) // 2
