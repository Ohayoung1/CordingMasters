'''
def catalan_number(n):
    # 카탈란 수를 계산하기 위한 리스트 초기화
    catalan = [0] * (n + 1)
    catalan[0] = 1  # C_0 = 1

    # 카탈란 수 계산
    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]

    return catalan[n]

def max_segments(N):
    if N % 2 != 0:
        return 0  # 교차하지 않게 그리려면 짝수개의 점이 필요합니다.

    # N개의 점을 연결할 수 있는 선분의 최대 개수는 N//2개의 카탈란 수를 구한 것과 같다
    return catalan_number(N // 2)

# 입력 받기
N = int(input())

# 결과 출력
print(max_segments(N))
'''
def max_segments(N):
   
    if N == 2:
        return 1
    
    increment = 0  

   
    for i in range(3,N):
        increment += 1  
    N += increment
    return N

N = int(input())


print(max_segments(N))
