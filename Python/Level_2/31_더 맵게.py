def solution(scoville, K):
    from heapq import heappush, heappop, heapify
    answer = 0
    heapify(scoville)
    while 1:
        if scoville[0] >= K:
            return answer
        if len(scoville) < 2:
            return -1
        answer += 1
        heappush(scoville, heappop(scoville) + 2*heappop(scoville))
