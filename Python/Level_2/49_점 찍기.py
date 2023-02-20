def solution(k, d):
    li = []
    answer = 0
    DD = d**2
    for i in range(0,d+1,k):
        j = int((DD - i**2)**0.5) // k
        answer += j + 1        
    return answer