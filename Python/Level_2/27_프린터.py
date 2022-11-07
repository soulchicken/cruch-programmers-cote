def solution(priorities, location):
    from collections import deque
    que = deque()
    priorities = deque(priorities)
    counts = [0]*10
    MAX = 0
    target = priorities[location]
    for num in priorities:
        counts[num] += 1
        MAX = max(MAX, num)
    answer = 1

    while 1:
        if MAX == target and not location:
            return answer
        if not counts[MAX]:
            MAX -= 1
            continue
        if priorities[0] == MAX:
            answer += 1
            location -= 1
            counts[MAX] -= 1

            priorities.popleft()
        else:
            priorities.append(priorities.popleft())
            if location:
                location -= 1
            else:
                location = len(priorities) - 1
