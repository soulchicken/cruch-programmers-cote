def solution(hp):
    return (hp // 15) * 3 + [0,1,2,1,2,1,2,3,2,3,2,3,4,3,4][hp % 15]