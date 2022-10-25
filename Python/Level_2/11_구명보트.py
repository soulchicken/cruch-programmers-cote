def solution(people, limit):
    from collections import deque
    people = deque(sorted(people))
    answer = 0
    while people:
        n = people.pop()
        if people and people[0] + n <= limit:
            people.popleft()
        answer += 1
    return answer