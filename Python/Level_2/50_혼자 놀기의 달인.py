def solution(cards):
    answer = 0
    LEN = len(cards)
    for i in range(LEN):
        cards[i] -= 1 # 인덱스
    MAX = 0
    for i in range(LEN):
        check = [0]*LEN
        box1 = []
        check[i] = 1
        box1.append(cards[i])
        card = cards[i]
        while 1:
            if check[card]:
                break
            check[card] = 1
            box1.append(cards[card])
            card = cards[card]
        if len(box1) == LEN:
            continue
        for j in range(LEN):
            if check[j]:
                continue
            box2 = []
            check2 = check[:]
            check2[j] = 1
            box2.append(cards[j])
            card = cards[j]
            
            while 1:
                if check2[card]:
                    break
                check2[card] = 1
                box2.append(cards[card])
                card = cards[card]
            score = len(box1) * len(box2)
            if score > MAX:
                MAX = score
    return MAX
