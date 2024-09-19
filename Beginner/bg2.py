'''
영덕이는 영어학원에 다니고 있습니다. 선생님은 매일 
학생들의 이름을 무작위로 나열한 비밀
목록을 만들고, 이름이 i번째로 나열된 학생에게 i번째 
문제의 정답을 발표시킵니다. 발표할 때 매번 틀린 답을 
하는 영덕이는 자신에게 크게 실망했습니다. 그래서 오늘,
영덕이는 비밀 목록을 몰래 보고 몇 번째 문제의 정답을 
발표해야 할지 미리 알아내려 합니다.

영덕이의 영어 이름을 포함한 N명의 이름이 적힌 목록이 
주어집니다. 이때 영덕이의 영어 이름이 목록에서 몇 
번째인지 출력하는 프로그램을 작성하세요.

입력 #1

5 BENJAMIN
GENNADY LINGYU ALEX BENJAMIN MIFAFA

입력 #2

10 G
A B C D E F G H I J

출력 #1

4

출력 #2

7
'''

n,name = map(str,input().split())
N = int(n)

names = input().split()

for i in range(N):
    if names[i] == name:
        print(i+1)
        break
    