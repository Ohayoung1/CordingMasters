'''
두정동에는 N개의 아파트 단지가 일직선상에 존재합니다. 
각 아파트 단지에는 
1번부터 N번까지 번호가 붙어있습니다.

두정동 동사무소에서는 아파트 단지 중 한 곳에 분리수거장을
지으려고 합니다. 분리수거장으로부터 각 주민들까지의 거리
의 합이 최소가 되도록 하려면 어떤 아파트 단지에 분리수거장
을 지어야 하는지 구하세요.

분리수거장으로부터 어떤 주민까지의 거리는 분리수거장이 
있는 아파트 단지의 위치와 해당 주민이 거주하는 아파트 
단지의 위치의 차로 계산됩니다.

단, 조건을 만족하는 아파트 단지가 여러개일 경우, 더 작은
번호의 아파트 단지에 분리수거장을 짓습니다.

입력 #1

7
475 170
28 95
506 8361
51 3988
2 977
607 793
49 847

입력 #2

11
998 2607
9422 3358
806 80622
2848 4153
398 180
867 22219
6514 806
246 9462
906 43046
2592 289
8 8486

출력 #1

3

출력 #2

3
'''

N = int(input())
apt = []
for i in range(N):
    d,a = map(int,input().split())
    apt.append((d,a))
    
md = float('inf')  # 최소 거리 합 초기화
best_index = -1  # 최적 아파트 단지 인덱스 초기화


for i in range(N):
    d_i,a_i = apt[i]
    td = 0
    
    for j in range(N):
        d_j,a_j = apt[j]
        td += abs(d_i - d_j) * a_j # 거리 합 계산

    if td < md :
        md = td
        best_index = i+1
    elif td == md and (i+1)<best_index:
        best_index = i+1


print(best_index)
        