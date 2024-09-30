'''
피보나치 수열이란 첫재 항과 둘째 항이 1이고, 그 뒤의 모든 항은 바로 앞의 두 항의 합인 수열입니다.
피보나치 피보나치 수열이란, 피보나치 수열의 각 항을 그 수만큼 반복해서 만든 수열을 말합니다.
예를 들어, 피보나치 피보나치 수열의 첫 10항은 다음과 같습니다.
1, 1, 2, 2, 3, 3, 3, 5, 5, 5, ...

a와 b가 주어졌을 때, 피보나치 피보나치 수열의 a항부터 b항까지의 합을 출력하는 프로그램을 작성해 주세요.

입력 #1

2 5

입력 #2

1 10

출력 #1

8

출력 #2

30
'''
def g_fibo(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def g_fib_fib(fib, length):
    fib_fib = []
    for f in fib:
        fib_fib.extend([f] * f)
        if len(fib_fib) >= length:
            break
    return fib_fib

def fibo(a, b):
    fib = g_fibo(12)
    fib_fib = g_fib_fib(fib, b)
    return sum(fib_fib[a-1:b])

a, b = map(int, input().split())
print(fibo(a, b))