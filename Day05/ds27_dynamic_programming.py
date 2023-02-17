# 피보나치 수열
# 한번 계산된 결과를 메모이제이션
d = [0] * 100

def fibonacci(n):
    if n == 0 or n == 1 or n == 2: return 1

    if d[n] != 0 : return d[n]

    d[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return d[n]

print('피보나치 수 --> 0 1', end=' ')
for i in range(2, 35):
    print(fibonacci(i), end=' ')