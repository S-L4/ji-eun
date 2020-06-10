def solution(s):
    s = s.lower()
    p_num = y_num = 0
    for alpha in s:
        if alpha == 'p':
            p_num += 1
        elif alpha == 'y':
            y_num += 1

    return p_num == y_num


# # 다른 사람 풀이
# def numPY(s):
#     return s.lower().count('p') == s.lower().count('y')