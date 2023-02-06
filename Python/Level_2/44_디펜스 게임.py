def solution(n, k, enemy):
    from heapq import heappush, heappop
    total = 0
    heap = []
    count = 0
    max_count = 0
    for e in enemy:
        count += 1
        total += e
        heappush(heap, -e)
        while total > n:
            if not k:
                return count - 1
            total += heappop(heap)
            k -= 1
    return count
