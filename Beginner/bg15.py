'''
오래된 궁전이 세월의 무게를 이기지 못하고 무너지려고 합니다. 관리당국에서는 궁전 곳곳에 
기둥을 세우는 보수 공사를 하려고 합니다. 직사각형 형태의 
궁전을 형성하는 모든 가로, 세로 줄에 대해서 적어도 기둥이 
하나씩은 존재하도록 만들고자 
할 때 세워야 하는 기둥의 최솟값을 출력하세요.

입력 #1

3 3
1 1 1
1 1 1
1 1 1

입력 #2

4 3
0 1 1
1 0 0
0 1 0
1 0 1

출력 #1

3

출력 #2

0
'''

def min_pillars_needed(N, M, palace):
    row_pillars = 0
    col_pillars = 0
    
    # 가로줄에서 기둥이 없는 줄을 세기
    for i in range(N):
        if 0 not in palace[i]:
            row_pillars += 1
    
    # 세로줄에서 기둥이 없는 줄을 세기
    for j in range(M):
        if all(palace[i][j] == 1 for i in range(N)):
            col_pillars += 1
    
    # 가로줄과 세로줄에서 더 많은 기둥이 필요한 쪽이 최소 기둥 개수
    return max(row_pillars, col_pillars)

# 입력 받기
N, M = map(int, input().split())
palace = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(min_pillars_needed(N, M, palace))

