def solution(keymap, targets):
    answer = []
    dic = dict()
    INF = float('inf')
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        dic[i] = INF

    for word in keymap:
        for a in range(len(word)):
            A = word[a]
            click = a + 1
            if dic[A] > click:
                dic[A] = click

    for target in targets:
        count = 0
        for a in target:
            if dic[a] == INF:
                count = -1
                break
            count += dic[a]
        answer.append(count)

    return answer
