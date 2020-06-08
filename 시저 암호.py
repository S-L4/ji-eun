def solution(s, n):
    answer = ''
    for word in s:
        if word.isupper():
            answer += chr((ord(word)-ord('A')+n)%26+ord('A'))
        elif word.islower():
            answer += chr((ord(word)-ord('a')+n)%26+ord('a'))
        else:
            answer += ' '
    return answer