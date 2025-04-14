# 1. ["apple", "banana", "cherry"] 리스트에 "orange" 추가
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("1. 과일 리스트:", fruits)

# 2. [10, 20, 30] 리스트의 모든 요소의 합 구하기
numbers = [10, 20, 30]
total = sum(numbers)
print("2. 숫자 합계:", total)

# 3. [1, 2, 3, 4, 5] 리스트의 요소를 역순으로 출력
lst = [1, 2, 3, 4, 5]
reversed_list = lst[::-1]
print("3. 역순 리스트:", reversed_list)

# 4. [5, 2, 8, 1, 9] 리스트 오름차순 정렬
nums = [5, 2, 8, 1, 9]
nums.sort()
print("4. 정렬된 리스트:", nums)