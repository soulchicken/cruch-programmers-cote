def solution(dartResult):
    dartResult = dartResult.replace('10','t')
    li = []
    for _ in range(2):
        for i in range(1,len(dartResult)):
            if dartResult[i].isdigit() or dartResult[i] == 't':
                li.append(dartResult[:i])
                dartResult = dartResult[i:]
                break
    li.append(dartResult)
    answer = []
    bonus = ['0','S','D','T']
    for dart in li:
        if dart[0] == 't':
            n = 10 ** bonus.index(dart[1])
        else:
            n = int(dart[0]) ** bonus.index(dart[1])
        answer.append(n)
        if len(dart) == 3:
            if dart[2] == '#':
                answer[-1] *= -1
            else:
                answer[-1] *= 2
                if len(answer) > 1:
                    answer[-2] *= 2
    return sum(answer)