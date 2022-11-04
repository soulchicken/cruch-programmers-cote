def solution(s):
    answer = s[2:-2].split('},{')
    li = [list(map(int,i.split(','))) for i in answer]
    li = sorted((len(i),i) for i in li)
    answer = []
    for _,i in li:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer