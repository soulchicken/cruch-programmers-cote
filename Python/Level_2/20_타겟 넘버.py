def solution(numbers, target):
    from collections import deque
    que = deque()
    que.append([0,0])
    answer = 0
    max_count = len(numbers)
    while que:
        total, count = que.pop()
        if count != max_count:
            que.append([total + numbers[count],count+1])
            que.append([total - numbers[count],count+1])
        elif total == target:
            answer += 1
    return answer