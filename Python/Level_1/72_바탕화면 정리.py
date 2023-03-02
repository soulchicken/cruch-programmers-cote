def solution(wallpaper):
    
    I = len(wallpaper)
    J = len(wallpaper[0])
    
    x1,y1 = 0,0
    x2,y2 = I-1,J-1
    for i in range(I):
        for j in range(J):
            if wallpaper[i][j] == '#':
                x1 = max(x1,i)
                x2 = min(x2,i)
                y1 = max(y1,j)
                y2 = min(y2,j)
    
    return [x2,y2,x1+1,y1+1]