# 총 금액과 인원수
total_money = 10000
people = 3

# 1인당 금액 (정수 나눗셈)
per_person = total_money // people

# 나머지 금액
remainder = total_money % people

# 출력
print(f"각자 받을 금액: {per_person}원")
print(f"남는 금액: {remainder}원")