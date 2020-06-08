def solution(s):
    return ''.join(sorted(list(s), key=lambda x: ord(x), reverse=True))



# 다른 사람 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))