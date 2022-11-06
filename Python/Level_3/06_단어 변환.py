def solution(begin, target, words):
    from collections import deque

    words = deque(words)
    words.appendleft(begin)

    dic = dict()
    LEN = len(words[0])
    for i in range(len(words)):
        I = words[i]
        dic[words[i]] = [i, []]
        for j in range(len(words)):
            count = 0
            J = words[j]
            for k in range(LEN):
                if I[k] != J[k]:
                    count += 1
            if count == 1:
                dic[I][1].append(J)

    que = deque()
    que.append((begin, 0))
    check = [float('inf')]*len(words)
    while que:
        word, count = que.popleft()
        idx, li = dic[word]
        if word == target:
            return count
        if check[idx] > count:
            check[idx] = count
            for new_word in li:
                que.append((new_word, count+1))
    return 0
