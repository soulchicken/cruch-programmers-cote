def solution(enroll, referral, seller, amount):
    dic = dict()
    dic['MINHO'] = ['MINHO', 0]
    for i in range(len(enroll)):
        name, refer = enroll[i], referral[i]
        if refer == '-':
            refer = 'MINHO'
        dic[name] = [refer, 0]
    for name, a in zip(seller, amount):
        money = a * 100
        while money > 9:
            temp = int(money * 0.1)
            dic[name][1] += money - temp
            name = dic[name][0]
            money = temp
        dic[name][1] += money
        money = 0
    answer = []
    for en in enroll:
        answer.append(dic[en][1])
    return answer
