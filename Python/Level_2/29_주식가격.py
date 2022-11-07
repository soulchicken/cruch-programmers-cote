def solution(prices):
    count = 0
    answer = [0]*len(prices)
    stack = []  # (price,idx,count)
    for idx in range(len(prices)):
        count += 1
        while stack and stack[-1][0] > prices[idx]:
            _, i, c = stack.pop()
            answer[i] = count - c
        stack.append((prices[idx], idx, count))
    while stack:
        _, i, c = stack.pop()
        answer[i] = count - c
    return answer
