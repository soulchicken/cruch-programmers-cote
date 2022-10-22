def solution(N, stages):
    # 실패율 : 스테이지 머뭄 / 스테이지 통과 + 스테이지 머뭄
    in_stage = [0]*(N+2)
    for i in stages: in_stage[i] += 1
    clear_stage = [0]*(N+2)
    clear_stage[-1] = in_stage[-1]
    for i in range(N,0,-1):
        clear_stage[i] = clear_stage[i+1] + in_stage[i]

    answer = sorted((1 - in_stage[i]/clear_stage[i],i) if clear_stage[i] else (1,i) for i in range(1,N+1))
    return [i for _,i in answer]