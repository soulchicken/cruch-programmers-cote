def solution(citations):
    count = len(citations)
    citations.sort()
    h = 0
    for i in citations:
        for j in range(h,i+1):
            if count >= j:
                h = j
        count -= 1
    return h