def solution(money):
    # 1번방을 고르고 2번방 안고름
    yes = [0]*len(money)
    no = [0]*len(money)
    yes[0] = money[0]
    no[1] = money[0]
    for i in range(2,len(money)-1):
        yes[i] = money[i] + max(no[i-1],yes[i-2])
        no[i] = max(yes[i-1],no[i-1])
    no[-1] = max(yes[-2],no[-2])
    answer = no[-1]
    # 1번방을 안고르고 2번방 고름
    yes = [0]*len(money)
    no = [0]*len(money)
    yes[1] = money[1]
    for i in range(2,len(money)):
        yes[i] = money[i] + max(no[i-1],yes[i-2])
        no[i] = max(yes[i-1],no[i-1])
    answer = max(answer,yes[-1],no[-1])

    yes = [0]*len(money)
    no = [0]*len(money)
    for i in range(2,len(money)):
        yes[i] = money[i] + max(no[i-1],yes[i-2])
        no[i] = max(yes[i-1],no[i-1])
    
    answer = max(answer,yes[-1],no[-1])

    # 1,2번방 둘 다 안고름
    return answer