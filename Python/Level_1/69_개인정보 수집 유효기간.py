def solution(today, terms, privacies):
    answer = []
    dic = dict()
    for term in terms:
        a, b = term.split()
        dic[a] = int(b)
    today = list(map(int, today.split('.')))
    li = []
    for pr in privacies:
        day, term = pr.split()
        day = list(map(int, day.split('.')))
        day[1] += dic[term]
        if day[1] > 12:
            d = day[1]
            day[1] %= 12
            day[0] += d // 12
            if not day[1]:
                day[1] = 12
                day[0] -= 1
        li.append(day)
    year, month, day = today
    if month < 10:
        month = '0'+str(month)
    if day < 10:
        day = '0' + str(day)
    today = int(str(year) + str(month) + str(day))
    li2 = []
    for i in li:
        y, m, d = i
        if m < 10:
            m = '0'+str(m)
        if d < 10:
            d = '0' + str(d)
        li2.append(int(str(y) + str(m) + str(d)))
    for i in range(len(li)):
        if li2[i] <= today:
            answer.append(i+1)
    return answer
