text = "Python is awesome"
vowels = "aeiou"

# 모두 소문자로 바꿔서 모음 검사
text = text.lower()

count = 0
for char in text:
    if char in vowels:
        count += 1

print("모음의 개수:", count)