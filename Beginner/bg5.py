'''
세아는 영어를 너무 좋아한 나머지 자기만의 영어사전을
만들려고 합니다. 머릿속에 떠오른 영어단어를
다음과 같은 기준에 따라 정리하려고 합니다.

우선, 길이가 짧은 단어부터 순서대로 나열합니다. 
만약 단어의 길이가 같다면 사전순대로 정리합니다. 세아가 
사전을 만드는 프로그램을 작성하세요.

입력 #1

3
apple
banana
coconut

입력 #2

6
monk
apply
angel
elephant
apply
encyclopedia

출력 #1

apple
banana
coconut

출력 #2

monk
angel
apply
elephant
encyclopedia
'''

n = int(input())
words = set()

for _ in range(n):
    word = input().strip()
    words.add(word)
    
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)