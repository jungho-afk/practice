# 사용자 입력 받기
email = input("이메일 주소를 입력하세요: ")

# 유효성 검사 조건: '@'와 '.'이 모두 포함되어 있어야 함
if "@" in email and "." in email:
    print("유효한 이메일 주소입니다.")
else:
    print("유효하지 않은 이메일 주소입니다.")