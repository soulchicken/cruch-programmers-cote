def solution(n, lost, reserve):
    answer = {i for i in range(1,n+1)} - set(lost)
    answer |=  set(reserve)
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)
    for i in sorted(reserve):
        if i-1 in lost:
            answer |= {i-1}
            lost -= {i-1}
        elif i+1 in lost:
            answer |= {i+1}
            lost -= {i+1}
    return len(answer)