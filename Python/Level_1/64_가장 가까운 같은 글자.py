def solution(s):
    answer = []
    # a == 97, z == 122
    li = [-1]*26
    for i in range(len(s)):
        n = ord(s[i]) - 97
        if li[n] == -1:
            answer.append(-1)
        else:
            answer.append(i - li[n])
        li[n] = i
    return answer
