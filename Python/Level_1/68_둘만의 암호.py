def solution(s, skip, index):
    answer = ''
    li = list('abcdefghijklmnopqrstuvwxyz')
    for a in skip:
        li.remove(a)
    li = ''.join(li) * 4
    for a in s:
        answer += li[li.index(a) + index]
    return answer
