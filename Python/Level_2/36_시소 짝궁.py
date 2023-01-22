def solution(weights):
    answer = 0
    N = [0]*1001
    for weight in weights:
        N[weight] += 1
    # 같은 숫자
    # 2와 4
    # 2와 3
    # 3과 4

    # 같은 숫자
    for i in range(1001):
        if N[i] > 1:
            answer += N[i] * (N[i] - 1)
    answer //= 2
    # 2 4
    for i in range(2, 1001, 2):
        answer += N[i] * N[i // 2]
    # 2 3
    for i in range(6, 2002, 6):
        answer += N[i // 2] * N[i // 3]
    # 3 4
    for i in range(12, 3003, 12):
        answer += N[i // 3] * N[i // 4]
    return answer
