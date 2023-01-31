def solution(numbers):
    answer = []
    stack = []
    while numbers:
        num = numbers.pop()
        while 1:
            if not stack:
                answer.append(-1)
                stack.append(num)
                break
            elif stack[-1] > num:
                answer.append(stack[-1])
                stack.append(num)
                break
            else:
                stack.pop()
    return answer[::-1]
