sum_of_multiples_of_3 = 0
for i in range(1, 101):
  if i % 3 == 0:
    sum_of_multiples_of_3 += i

print("1부터 100까지 3의 배수의 합:", sum_of_multiples_of_3)