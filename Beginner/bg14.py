'''
또리에게는 시:분:초를 출력하는 디지털시계가 있습니다. 
매일매일은 00:00:00부터23:59:59까지의 초로 표현됩니다.
방학이 되어 지루해진 또리는 하루 종일 디지털시계를 
쳐다보면서 숫자 N이 몇 번 등장하는지 세어보기로 했습니다. 
숫자를 모두 세어본 또리는 문득 본인이 맞게 세었는지 
궁금해졌습니다.
또리를 위해 하루 동안 숫자 N을 볼 수 있는 시간은 몇 
초인지 구하는 프로그램을 작성하세요.

예를 들어 N = 3일 때는 00:00:00부터 23:59:59까지 
3이라는 숫자가 포함된 시간이 총 43875초 이므로 43875를
출력하면 됩니다.

입력 #1

1

입력 #2

3

출력 #1

62100

출력 #2

43875
'''

n = int(input())
count = 0
N_str = str(n)

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            time_str = f"{hour:02}:{minute:02}:{second:02}"
            
            if N_str in time_str:
                count += 1
print(count)