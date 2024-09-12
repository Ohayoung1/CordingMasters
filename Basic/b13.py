#우리반 아이큐왕은

'''
신화중학교 3학년 2반 학생들은 며칠 전 IQ검사를 치루었고, 
드디어 오늘 결과가 나왔습니다. 학생들은 반에서 IQ가 높은 
학생이 누구인지 궁금해졌습니다. 학생들의 이름과 IQ가 
입력될 때, IQ가 높은 순서대로 상위 3명의 이름을 출력하는 
프로그램을 만드세요. IQ가 같을 경우에는 
먼저 입력된 학생의 이름을 출력합니다.

입력 #1

4
jung 51
dong 160
back 120
pang 89

입력 #2

7
jang 180
nana 125
min 125
hani 142
kwan 170
hyun 97
jack 86

출력 #1

dong
back
pang

출력 #2

jang
kwan
hani
'''

def top_st(N,s):
    #학생 데이터를 iq를 기준으로 정렬(내림차순)
    s = sorted(s,key = lambda x:x[1],reverse=True)
    
    #상위 3명의 이름 출력
    for i in range(3):
        print(s[i][0])


n = int(input())

student = []

for _ in range(n):
    name, iq = input().split()
    iq = int(iq)
    student.append((name,iq))
    
top_st(n,student)