# 총 초
total_seconds = 12345

# 시간 계산
hours = total_seconds // 3600

# 남은 초에서 분 계산
minutes = (total_seconds % 3600) // 60

# 남은 초 계산
seconds = total_seconds % 60

# 결과 출력
print(f"{total_seconds}초는 {hours}시간 {minutes}분 {seconds}초입니다.")