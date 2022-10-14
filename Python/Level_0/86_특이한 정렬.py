def solution(numlist, n):
    return [i for _,_,i in sorted([abs(val - n),10000-val,val] for idx,val in enumerate(numlist))]