'''
삼각형의 세 변의 길이가 주어집니다. 이 삼각형이 직각삼각형인지 판별하는 프로그램을 작성해 주세요.

입력 #1

3 4 5

입력 #2

5 6 7

출력 #1

YES

출력 #2

NO
'''
a,b,c = map(int,input().split())

if a > b and a > c :
    if a*a == (b*b)+(c*c):
        print("YES")
    else:
        print("NO")
elif b > a and b > c :
    if b*b == (c*c)+(a*a):
        print("YES")
    else:
        print("NO")
elif c > a and c > b :
    if c*c == (b*b)+(a*a):
        print("YES")
    else:
        print("NO")
elif a == c == b:
    print("NO")
        