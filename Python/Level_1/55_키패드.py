def solution(numbers, hand):
    l,r = [3,0],[3,2]
    answer = ''
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            l = [n//3,0]
        elif n in [3,6,9]:
            answer += 'R'
            r = [(n-1)//3,2]
        else:
            if n == 0:
                n = 11
            c = [(n)//3,1]
            l_gap = abs(c[0]-l[0])+abs(c[1]-l[1])
            r_gap = abs(c[0]-r[0])+abs(c[1]-r[1])
            if l_gap > r_gap or (l_gap == r_gap and hand == 'right'):
                answer += 'R'
                r = [n//3,1]
            else:
                answer += 'L'
                l = [n//3,1]
    return answer