'''
N개의 한 자리 정수들이 주어졌을 때 이 정수들을 서로 
이어붙여 만들 수 있는 가장 큰 300의 배수를 구하는 프
로그램을 작성하세요. 

이 때, 주어진 모든 정수를 사용해야 합니다. 
예를 들어 3, 6, 9, 0, 5, 0, 7, 6이 주어졌을 때 만들
수 있는 가장 큰 300의 배수는 97665300입니다.

0 또한 300의 배수임에 유의합니다.

입력 #1

4
2 4 0 0

입력 #2

4
3 6 0 3

출력 #1

4200

출력 #2

-1
'''

def largest_300_multiple(nums):
    nums.sort(reverse=True)
    
    if nums.count(0) < 2:  # 0이 두 개 미만이면 100의 배수를 만들 수 없음
        return -1
    
    if sum(nums) % 3 != 0:  # 숫자의 합이 3의 배수가 아니면 300의 배수를 만들 수 없음
        return -1
    
    if nums[0] == 0:  # 모든 숫자가 0일 경우 0을 반환
        return 0
    
    return int(''.join(map(str, nums)))

N = int(input())
nums = list(map(int, input().split()))

# 모든 입력이 0일 때는 0만 출력
if set(nums) == {0}:
    print(0)
else:
    print(largest_300_multiple(nums))