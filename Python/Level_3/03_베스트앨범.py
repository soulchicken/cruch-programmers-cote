def solution(genres, plays):
    # 장르당 2개씩
    # 많이 재생된 장르 먼저
    # 장르 내 동일 조건, 고유번호가 낮은 순
    dic = dict()
    for i in range(len(plays)):
        g = genres[i]
        p = plays[i]
        if g not in dic:
            dic[g] = [0,[]]
        dic[g][0] += p
        dic[g][1].append((-p,i))
    li = []
    for val in dic.values():
        val[1].sort()
        li.append(val)
    li.sort()
    answer = []
    while li:
        _,songs = li.pop()
        answer.append(songs[0][1])
        if len(songs) > 1:
            answer.append(songs[1][1])
        
    return answer