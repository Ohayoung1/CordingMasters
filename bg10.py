'''
월미도 게임랜드에는 두더지 게임 기계가 있습니다. 
기계는 8 X 8 칸의 판으로 이루어져 있고, 
모양은 이러합니다.

0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0
0 1 0 1 0 1 0 1
1 0 1 0 1 0 1 0


두더지는 0에 해당하는 위치에서만 올라올 수 있습니다. 
1에 해당하는 칸에서는 두더지가 존재한다 해도 구멍이 막혀
있어 올라올 수 없습니다. 
기계 아래 어느 칸에 두더지가 있는지에 대한 정보가 주어질
때, 두더지가 올라올 수 있는 칸의 개수를 알아내는 
프로그램을 작성하세요.

입력 #1

TFFTTFTT
FTFTFTTF
TTTFTFTT
TTTTFFTT
TFTTFTFT
TTTFFTTF
TFTFTFTT
TFTFTTFT

입력 #2

TFFTTFTT
FTFTFTTF
TTTFFTTF
TFTFTFTT
TFTFTTFT
TTTFFTTF
TFFTTFTT
FTFTFTTF

출력 #1

9

출력 #2

11
'''
def count_moles(board):
    count = 0
    pattern = [
        ['0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0'],
        ['0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0'],
        ['0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0'],
        ['0', '1', '0', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '1', '0']
    ]
    
    for i in range(8):
        for j in range(8):
            if pattern[i][j] == '0' and board[i][j] == 'F':
                count += 1
    return count


board = [input().strip() for _ in range(8)]  


result = count_moles(board)

