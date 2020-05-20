def solution(n):
    answer = ''

    n -= 1
    while n >= 0:
        if n%3 == 0: answer += '1'
        elif n%3 == 1: answer += '2'
        elif n%3 == 2: answer += '4'
        n //= 3; n -= 1
        
    return answer