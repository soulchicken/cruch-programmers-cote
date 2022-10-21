def solution(sizes):
    a, b=0, 0
    for i,j in sizes: a,b = max(a,i,j),max(b,min(i,j))
    return a * b