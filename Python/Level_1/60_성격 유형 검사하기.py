def solution(survey, choices):
    m = 'RTCFJMAN'
    mbti = dict(zip(list('RTCFJMAN'),[0]*8))
    for i in range(len(choices)):
        if choices[i] == 4:
            continue
        c = survey[i][choices[i] // 4]
        if choices[i] < 4:
            n = 4 - choices[i]
        else:
            n = choices[i] - 4
        mbti[c] += n

    answer = ''
    for i in range(0,8,2):
        a,b = m[i],m[i+1]
        x,y = mbti[a],mbti[b]
        if x >= y:
            answer += a
        else:
            answer += b
    return answer