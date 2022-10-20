def solution(arr1, arr2):
    return [[a+b for a,b in zip(i,j)] for i,j in zip(arr1,arr2)]