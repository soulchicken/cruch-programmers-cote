def solution(board):
    move = [[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[-1,0]]
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            for x,y in move:
                if board[i][j] != 1 and 0<=i+x<len(board) and 0<=j+y<len(board) and board[i+x][j+y] == 1:
                    board[i][j] = 2
                    break
            if board[i][j] == 0: 
                answer += 1
    return answer