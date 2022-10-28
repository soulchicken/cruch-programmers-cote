def solution(operations):
    from heapq import heappush, heappop
    heap = []
    heap2 = []
    heaps = [0,heap,heap2]
    check = [1]*len(operations)
    for i in range(len(operations)):
        key, num = operations[i].split()
        num = int(num)
        if key == 'D':
            while heaps[num]:
                n,index = heappop(heaps[num])
                if check[index]:
                    check[index] = 0
                    break
        else:
            heappush(heap,(-num,i))
            heappush(heap2,(num,i))
    answer = []
    print(heap)
    for v,i in heap2:
        if check[i]:
            answer.append(v)
    return [max(answer),min(answer)] if answer else [0,0]