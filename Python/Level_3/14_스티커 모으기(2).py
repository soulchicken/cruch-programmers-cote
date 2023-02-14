def solution(sticker):
    answer = 0
    N = len(sticker)
    if N == 1:
        return sticker[-1]
    li1 = [0]*(N-1)
    li2 = [0]*(N-1)

    li1[0] = sticker[0]  # 첫 스티커를 씀

    for i in range(1, N-1):
        li1[i] = sticker[i] + li2[i-1]
        li2[i] = max(li1[i-1], li2[i-1])

    answer = max(li1[-1], li2[-1])

    li1 = [0]*N
    li2 = [0]*N

    li1[1] = sticker[1]
    for i in range(1, N):
        li1[i] = sticker[i] + li2[i-1]
        li2[i] = max(li1[i-1], li2[i-1])

        answer = max(answer, li1[-1], li2[-1])

    return answer
