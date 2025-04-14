# 사용자 입력 받기
weight = float(input("체중(kg)을 입력하세요: "))
height_cm = float(input("키(cm)를 입력하세요: "))

# 키를 미터(m) 단위로 변환
height_m = height_cm / 100

# BMI 계산
bmi = weight / (height_m ** 2)

# 결과 출력
print(f"BMI는 {bmi:.2f}입니다.")