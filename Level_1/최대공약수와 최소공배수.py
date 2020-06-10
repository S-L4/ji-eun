divisor = [[1] for _ in range(1000001)]
for i in range(2,1000001//2+1):
    j = 1
    while i*j < 1000001:
        divisor[i*j].append(i)
        j += 1

def solution(n, m):
    if n > m:
        n, m = m, n
    divisor[n].append(n)
    for num in divisor[n][::-1]:
        if not m%num:
            gcd = num
            break
    return [gcd, n*m//gcd]