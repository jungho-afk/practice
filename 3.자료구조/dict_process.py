# 1. {"name": "John", "age": 30} 딕셔너리에서 "age"의 값 출력
person = {"name": "John", "age": 30}
print("1. 나이:", person["age"])

# 2. {"math": 90, "science": 85, "history": 78}에서 모든 과목명 출력
scores = {"math": 90, "science": 85, "history": 78}
print("2. 과목명:", list(scores.keys()))

# 3. {'apple': 3, 'banana': 5}에서 apple의 값을 2 증가
fruits = {'apple': 3, 'banana': 5}
fruits['apple'] += 2
print("3. apple 개수:", fruits['apple'])

# 4. [5, 2, 8, 1, 9] 리스트 오름차순 정렬
nums = [5, 2, 8, 1, 9]
nums.sort()
print("4. 정렬된 리스트:", nums)