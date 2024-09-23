'''
민수와 진희는 계단을 내려가다가 재밌는 생각이 떠올라
게임을 하려고 합니다. 게임의 규칙은 간단합니다. 진희는 
가만히 있고, 민수는 진희와 다른 위치에서 시작합니다. 
민수는 계단을 세 칸 위로 올라가거나 한 칸 아래로 내려갈 
수 있습니다. 다른 방법으로 움직이는 경우는 없습니다. 
민수가 최소한의 횟수로 움직여 
진희와 같은 계단에 도착하는 프로그램을 만드세요.


입력 #1

3 40

입력 #2

23 145

출력 #1

15

출력 #2

42
'''
from collections import deque
def min_moves(n,k):
    queue = deque([(n,0)])
    visited = [False] * 100001
    visited[n] = True
    
    while queue:
        current,moves= queue.popleft()
        
        if current == k:
            return moves
        
        next_positions = [current +3,current -1]
        
        for next_pos in next_positions:
            if 1 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, moves +1))

n,k = map(int,input().split())

print(min_moves(n,k))
