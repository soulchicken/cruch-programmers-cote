def solution(arrayA, arrayB):
    answer = 0
    # 최소공배수를 일단 구하기
    from math import gcd
    A = arrayA[0]
    for i in range(1, len(arrayA)):
        A = gcd(A, arrayA[i])

    B = arrayB[0]

    for i in range(1, len(arrayB)):
        B = gcd(B, arrayB[i])
    print(A, B)
    flag = 1
    for i in arrayB:
        if i >= A and not i % A:
            flag = 0
            break
    if flag:
        answer = A
    flag = 1
    for i in arrayA:
        if i >= B and not i % B:
            flag = 0
            break
    if flag:
        answer = max(answer, B)
    return answer
