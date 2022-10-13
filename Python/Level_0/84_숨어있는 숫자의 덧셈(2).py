def solution(my_string):
    answer = 0
    stack = []
    for i in my_string:
        if i.isdigit():
            stack.append(i)
        elif stack:
            answer += int(''.join(stack))
            stack = []
    if stack:
        answer += int(''.join(stack))
    return answer