def solution(book_time):
    def time_count(s):
        A, B = map(int,s.split(":"))
        return 60*A + B
    
    book = []
    for a,b in book_time:
        A = time_count(a)
        B = time_count(b) + 10
        book.append((A,B))
        
    book.sort()
    
    from heapq import heappush, heappop
    
    heap = []
    answer = 0
    LEN = 0
    for A,B in book:
        while heap and heap[0] <= A:
            heappop(heap)
            LEN -= 1
        heappush(heap, B)
        LEN += 1
        
        if LEN > answer:
            answer = LEN
        
    return answer