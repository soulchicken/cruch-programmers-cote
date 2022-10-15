def solution(keyinput, board):
    max_a, max_b = board[0] // 2, board[1] // 2
    min_a, min_b = -max_a, -max_b
    x,y = 0,0
    for i in keyinput:
        if i == 'left':
            x = max(x-1,min_a)
        elif i == 'right':
            x = min(x+1,max_a)
        elif i == 'up':
            y = min(y+1,max_b)
        else:
            y = max(y-1,min_b)
    return [x,y]