def solution(answers):
    a,b,c = [1,2,3,4,5]*2000,[2,1,2,3,2,4,2,5]*1250,[3,3,1,1,2,2,4,4,5,5]*1000
    x,y,z=0,0,0
    for i in range(len(answers)):
        if answers[i]==a[i]:x+=1
        if answers[i]==b[i]:y+=1
        if answers[i]==c[i]:z+=1
    return [i+1 for i,v in enumerate([x,y,z]) if v == max(x,y,z)]