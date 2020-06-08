prime_numbers = [True]*1000001
for i in range(2,1000001//2):
    j = 2
    while i*j < 1000001:
        if prime_numbers[i*j]:
            prime_numbers[i*j] = False
        j += 1

def solution(n):
    return sum(prime_numbers[2:n+1])



# # 다른 사람 풀이
# def solution(n):
#     num = set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num -= set(range(2*i,n+1,i))

#     return len(num)