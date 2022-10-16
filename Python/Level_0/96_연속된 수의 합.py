def solution(num, total):
    return [i+1 + (total - ((1+ num)*num // 2)) // num for i in range(num)]