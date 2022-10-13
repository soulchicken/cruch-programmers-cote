def solution(emergency):
    return [j for _,j in sorted([[val,len(emergency)-idx] for idx,val in enumerate(emergency)])]