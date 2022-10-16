def f(x1,y1,x2,y2):
    if x1 - x2:
        return (y1-y2) / (x1-x2)
    return float('inf')
def solution(dots):
    answer = 0
    for i in range(4):
        for j in range(i+1,4):
            li = [0,1,2,3]
            li.pop(j)
            li.pop(i)
            if f(*dots[i],*dots[j]) == f(*dots[li[0]],*dots[li[1]]):
                return 1
    return 0