# 1. "Hello"와 "World"를 연결하여 "Hello World" 출력
a = "Hello"
b = "World"
result = a + " " + b
print("1. 연결 결과:", result)

# 2. 대문자로 변환
upper_result = result.upper()
print("2. 대문자 변환:", upper_result)

# 3. "World"만 슬라이싱
sliced = result[6:]
print("3. 'World' 슬라이싱:", sliced)

# 4. "Python is fun" 문자열 분리
sentence = "Python is fun"
words = sentence.split()
print("4. 문자열 분리:", words)

# 5. "abcdef"에서 짝수 인덱스 문자 출력
text = "abcdef"
even_index_chars = text[::2]
print("5. 짝수 인덱스 문자:", even_index_chars)

# 6. "Hello"를 3번 반복
repeated = "Hello" * 3
print("6. 'Hello' 3번 반복:", repeated)