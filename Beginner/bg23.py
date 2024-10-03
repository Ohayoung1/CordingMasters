'''
수학자 가우스는 1796년에 다음과 같은 사실을 보였습니다. 

- 어떤 정다각형이 작도가능할 필요충분조건은, 그 변의 개수가 서로 다른 페르마 소수의 곱과 2의 거듭제곱을 곱한 형태로 나타나지는 것이다.

페르마 소수란 음이 아닌 정수 n에 대하여 F_n = 2^(2^n)+1 꼴로 나타내어지는 소수를 말하고, 지금까지 알려진 페르마 소수는 다음과 같습니다. (적어도 10¹? 이하의 자연수 중에 페르마 소수는 다음 5개 밖에 없음이 증명되어 있습니다.)

- F_0 = 2¹ + 1 = 3
- F_1 = 2² + 1 = 5
- F_2 = 2⁴ + 1 = 17
- F_3 = 2? + 1 = 257
- F_4 = 2¹? + 1 = 65537

이 때 작도 가능한 정다각형의 예시를 들면 다음과 같습니다. 

- 정4각형, 정8각형, 정16각형, … (1도 서로 다른 페르마 소수의 곱으로 생각합니다.)
- 정3각형, 정5각형, 정17각형, 정257각형, 정65537각형
- 정15각형(3×5), 정4369각형(17×257), 정3342387각형(3×17×65537)
- 정80각형(5×2⁴), 정204각형(3×17×2²), 정6291552각형(3×65537×2?)

어떤 정수 k가 주어질 때, 정k각형이 작도 가능한 정다각형인지 판별하는 프로그램을 작성해봅시다.
입력 #1

17

입력 #2

19

출력 #1

YES

출력 #2

NO

'''
'''
def is_power_of_two(N):
    return(N&N(N-1)) == 0
n = int(input())
n = n-1
if is_power_of_two(n):
    print("YES")
else:
    print("NO")
'''
'''
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
def is_constructible_polygon(k):
    if k < 3:
        return "NO"

    fermat_primes = [3, 5, 17, 257, 65537]
    
    # k를 페르마 소수의 곱으로 나누기
    for prime in fermat_primes:
        while k % prime == 0:
            k //= prime
            if k ==1 :
                return "YES"
            elif k== 2:
                return "NO"
            else:
                if is_power_of_two(k):
                    return "YES"
                else:
                    return "NO"

# 입력 받기
k = int(input())

# 결과 출력
print(is_constructible_polygon(k))
'''
def is_constructible_polygon(k):
    if k < 3:
        return "NO"

    # 페르마 소수 목록
    fermat_primes = [3, 5, 17, 257, 65537]
    
    # k를 페르마 소수의 곱으로 나누기
    for prime in fermat_primes:
        count = 0  # 각 소수의 나눌 수 있는 횟수
        while k % prime == 0:
            k //= prime
            count += 1
        # 페르마 소수가 제곱 이상으로 나누어진 경우
        if count >= 2:
            return "NO"

    # k가 2인 경우도 NO
    if k == 2:
        return "NO"

    # k를 2의 거듭제곱으로 나누기
    while k % 2 == 0:
        k //= 2
    
    # 남은 k가 1이면 "YES", 아니면 "NO"
    return "YES" if k == 1 else "NO"

# 입력 받기
k = int(input())

# 결과 출력
print(is_constructible_polygon(k))
