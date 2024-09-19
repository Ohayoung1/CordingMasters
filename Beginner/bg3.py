'''
N개의 서로 다른 정수가 정렬된 상태로 입력이 될 때 
특정한 원소 A가 몇 번째에 위치해 있는지 알려주는 
프로그램을 작성하세요. 
단 특정한 원소 A를 찾을 수 없을 때는 -1을 출력합니다.

입력 #1

10 7
1 2 3 4 5 6 7 8 9 10

입력 #2

5 9
1 3 5 7 9

출력 #1

7

출력 #2

5
'''

n,a = map(int,input().split())
k = list(map(int,input().split()))

found = False
for i in range(n):
    if k[i] == a:
        print(i+1)
        found = True
        break
    
if not found:
    print(-1)
    