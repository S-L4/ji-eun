divisors = [0] + [1]*3000
for i in range(2,3001):
    j = 1
    while i*j < 3001:
        divisors[i*j] += i
        j += 1

def solution(n):
    return divisors[n]



# # 다른 사람 풀이
# def sumDivisor(num):
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])