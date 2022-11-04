def solution(s):
    from collections import deque
    s = deque(list(s))
    answer = 0
    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif stack:
                if stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                elif stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                elif stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                else:
                    stack.append(s[i])
                    break
            else:
                stack.append(s[i])
                break
        if not stack:
            answer += 1
        s.append(s.popleft())
    return answer