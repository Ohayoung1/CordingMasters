'''
중앙값은 전체 데이터를 오름차순으로 정렬했을 때 
가운데에 있는 수치 값입니다.
중앙값은 극단적인 값이 있을 때 평균보다 데이터의 
대표값으로 더 유용합니다. 
예를 들어 직원이 100명인 회사에서 직원들 연봉 평균은
5천만원인데 사장의 연봉이 100억인 경우 중앙값이 평균보다
회사의 연봉을 나타내는 대표값으로 더 적합합니다.

5개의 정수에 대해서 중앙값을 찾아내는 프로그램을 
작성하세요.

입력 #1

101 2 100 1 102

입력 #2

7 18 38 5 40

출력 #1

100

출력 #2

18
'''

numbers = list(map(int, input().split()))
numbers.sort()
median = numbers[2]
print(median)