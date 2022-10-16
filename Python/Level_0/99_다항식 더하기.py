def solution(polynomial):
    polynomial = polynomial.replace('+ ','').split()
    x = 0
    n = 0
    for i in polynomial:
        if i == 'x':
            x += 1
        elif i[-1] == 'x':
            x += int(i[:-1])
        else:
            n += int(i)
    if x and n:
        if x != 1:
            return f'{x}x + {n}'
        else:
            return f'x + {n}'
    elif x:
        if x != 1:
            return f'{x}x'
        else:
            return 'x'
    else:
        return f'{n}'