def solution(s):
    stack = []
    for i in s.split():
        if i == 'Z' and stack:stack.pop()
        else: stack.append(i)
    return sum(map(int,stack))