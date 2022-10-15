def solution(sides):
    return len(range(max(sides)-min(sides)+1,max(sides)+1)) + len(range(max(sides)+1,sum(sides)))