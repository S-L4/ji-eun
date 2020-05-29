def solution(a, b):
    if a == b:
        answer = a
    elif a > b:
        answer = a*(a+1)//2 - (b-1)*b//2
    else:
        answer = b*(b+1)//2 - (a-1)*a//2
    return answer


# # 다른 사람의 풀이
# def adder(a, b):
#     if a > b: a, b = b, a

#     return sum(range(a,b+1))