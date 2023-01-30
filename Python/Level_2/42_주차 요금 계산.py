def solution(fees, records):
    answer = []
    basic_time, basic_fee, time, fee = fees
    dic = dict()
    cars = []
    for record in records:
        t, num, io = record.split()
        a, b = map(int, t.split(":"))
        t = a*60 + b
        if num not in dic:
            cars.append(num)
            dic[num] = [0]
        if io == 'IN':
            dic[num].append(t)
        else:
            n = dic[num].pop()
            dic[num][0] += t - n
    T = 23*60 + 59

    for key in cars:
        if len(dic[key]) == 2:
            n = dic[key].pop()
            dic[key][0] += T - n

    cars.sort()
    for car in cars:
        t = dic[car][0]
        t = max(0, t - basic_time)
        if t % time:
            t += time
        answer.append(fee*(t // time) + basic_fee)

    return answer
