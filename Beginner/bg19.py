'''
주사위 2개를 굴려 합이 N이 나오는 경우의 수를 구하는 
프로그램을 작성하세요. 반드시 주사위 2개를 함께 굴리며, 
예를 들어 N = 5일 때는 (1, 4), (2, 3), (3, 2), (4, 1)의 
네 가지 경우의 수가 존재합니다.

입력 #1

5

입력 #2

7

출력 #1

1 4
2 3
3 2
4 1

출력 #2

1 6
2 5
3 4
4 3
5 2
6 1
'''

n = int(input())
dice = []
for i in range(1,7):
    for j in range(1,7):
        if i + j == n:
            dice.append((i,j))

for dices in dice:
    print(dices[0],dices[1])