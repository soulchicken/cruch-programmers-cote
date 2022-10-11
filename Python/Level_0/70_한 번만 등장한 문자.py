def solution(s):
    li = [0]*26
    for i in s:
        li[ord(i) - ord('a')] += 1
    answer = ""
    for i in range(26):
        if li[i] == 1:
            answer += chr(ord('a') + i)
    return answer