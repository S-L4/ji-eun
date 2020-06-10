def solution(s):
    answer = False
    if sorted(s)[-1].isdecimal():
        if len(s) == 4 or len(s) == 6:
            answer = True
    return answer

# # 다른 사람 풀이
# def alpha_string46(s):
#     return s.isdigit() and len(s) in (4, 6)