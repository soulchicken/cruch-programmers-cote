def solution(k, score):
    from heapq import heappush, heappop
    answer = []
    heap = []

    for s in score:
        heappush(heap, s)
        if len(heap) > k:
            heappop(heap)
        answer.append(heap[0])

    return answer
