num_1 = input('Введите целое положительное число ')
num_1 = int(num_1)
num_2 = num_1%10
num_1 = num_1//10
while num_1 > 0:
    if num_1%10 > num_2:
       num_2 = num_1%10
    num_1 = num_1//10
print(num_2)

