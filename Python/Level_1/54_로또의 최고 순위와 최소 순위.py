def solution(lottos, win_nums):
    count = 0
    for i in lottos:
        for j in win_nums:
            if i == j: count += 1
    zero = count + lottos.count(0)
    win = [6,6,5,4,3,2,1]
    return [win[zero], win[count]]