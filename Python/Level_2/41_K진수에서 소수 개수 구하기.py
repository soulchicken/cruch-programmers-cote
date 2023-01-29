def solution(n, k):

    string = ""
    while n:
        string = str(n % k) + string
        n //= k

    li = []
    for s in string.split('0'):
        if s:
            li.append(int(s))
    li.sort()

    answer = 0
    for num in li:
        if num < 2:
            continue
        flag = 1
        for i in range(2, int(num**0.5) + 1):
            if not num % i:
                flag = 0
                break

        answer += flag
    return answer
