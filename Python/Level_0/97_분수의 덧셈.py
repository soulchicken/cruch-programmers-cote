def solution(denum1, num1, denum2, num2):
    a=denum1*num2+denum2*num1
    b=num1*num2
    for i in range(min(a,b),0,-1):
        if a%i + b%i == 0:
            break
    return [a//i,b//i]