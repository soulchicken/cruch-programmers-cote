def solution(arr):
    answer = arr[0]
    for n in arr:
        a = answer
        b = n
        while b != 0:
            a,b = b, a%b
        answer *= n
        answer //= a
    return answer