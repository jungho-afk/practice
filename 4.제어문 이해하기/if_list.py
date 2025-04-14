scores = [70, 85, 90, 55, 78]
passing_scores = []

for score in scores:
  if score >= 60:
    passing_scores.append(score)

print("합격한 점수:", passing_scores)