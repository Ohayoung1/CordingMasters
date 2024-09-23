'''
1부터 N까지의 숫자를 일렬로 늘어놓았을 때, 0부터 
9까지의 숫자가 각각 
몇 번씩 나오는지 알아내는 프로그램을 만드세요.

입력 #1

12

입력 #2

321

출력 #1

1 5 2 1 1 1 1 1 1 1

출력 #2

62 173 164 84 62 62 62 62 62 62
'''
def count_digits(n):
    digit_count = [0] * 10
    
    for i in range(1,n+1):
        for digit in str(i):
            digit_count[int(digit)] +=1
        
    return digit_count

n = int(input())
result = count_digits(n)

print(' '.join(map(str,result)))
