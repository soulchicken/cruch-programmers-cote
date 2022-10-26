def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    for i in new_id:
        if i.isdigit() or i.isalpha() or i in ['-','_','.']:
            answer += i
    while '..' in answer:
        answer = answer.replace('..','.')
    answer = answer.strip('.')
    if not answer: answer = 'a'
    if len(answer) > 15: answer = answer[:15]
    answer = answer.strip('.')
    if not answer: answer = 'a'
    while len(answer) < 3:
        answer += answer[-1]
    return answer