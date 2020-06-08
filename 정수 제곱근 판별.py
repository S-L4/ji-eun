square_numbers = set(i**2 for i in range(7071068))

def solution(n):
    return (n**0.5+1)**2 if n in square_numbers else -1


# # 다른 사람 풀이
# def nextSqure(n):
#     sqrt = n ** (1/2)

#     if sqrt % 1 == 0:
#         return (sqrt + 1) ** 2
#     return -1