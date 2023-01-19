def solution(s):
    answer = 0
    while s:
        x = s[0]
        cnt1 = 0
        cnt2 = 0
        for i in range(len(s)):
            if x == s[i]:
                cnt1 += 1
            else:
                cnt2 += 1
            if cnt1 == cnt2:
                answer += 1
                print(s[:i+1])
                s = s[i+1:]
                break
            if i == len(s) - 1:
                return answer+1
    return answer
