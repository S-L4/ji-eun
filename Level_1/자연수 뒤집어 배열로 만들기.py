def solution(n):
    return list(reversed([int(x) for x in str(n)]))


# # 다른 사람 풀이
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))

# def digit_reverse(n):
#     return [int(i) for i in str(n)][::-1]