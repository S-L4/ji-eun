def solution(s):
    answer = ''; i = 0
    for word in s:
        if word.isalpha():
            if i%2:
                answer += word.lower()
            else:
                answer += word.upper()
            i += 1
        else:
            answer += ' '
            i = 0
    return answer



# # 다른 사람 풀이
# def toWeirdCase(s):
#     return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split()])