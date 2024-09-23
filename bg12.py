'''
정수 A와 B가 입력될 때 A개의 원소에서 B개의 원소를 
뽑는 조합에 대한 총 경우의
수를 출력하는 프로그램을 작성하세요.

입력 #1

10 5

입력 #2

7 2

출력 #1

252

출력 #2

21
'''
import math
def combinations(a,b):
    
    return math.comb(a,b)
a,b = map(int,input().split())
print(combinations(a,b))