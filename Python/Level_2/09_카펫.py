def solution(brown, yellow):
    brown += yellow
    for i in range(1,yellow+1):
        x = yellow % i + brown%(i+2) == 0
        y = brown // (i +2) == yellow//i + 2
        if x and y: return [brown // (i+2), i + 2]