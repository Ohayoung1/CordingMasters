'''
많은 워드프로세서들은 문서에 대한 통계를 제공합니다. 
한 줄 분량의 문서가 주어졌을 때, 이 문서에 대한 
통계를 출력하는 프로그램을 작성해 주세요.

입력 #1

Coding Masters

입력 #2

A(공백)B(공백)(공백)C(공백)D(공백)(공백)(공백)E

출력 #1

14
13
2

출력 #2

12
5
5
'''

def document_statistics(text):
 
    total_characters = len(text)
    
   
    non_space_characters = len(text.replace(" ", ""))
    
    # 단어 수 (공백으로 분리된 부분의 수)
    words = text.split()
    word_count = len(words)
    
    return total_characters, non_space_characters, word_count


input_text = input()


total_chars, non_space_chars, word_count = document_statistics(input_text)


print(total_chars)
print(non_space_chars)
print(word_count)
