def solution(array):
    a,b = 0,0
    for i in range(len(array)):
        if array[i] > a: a,b = array[i],i
    return [a,b]