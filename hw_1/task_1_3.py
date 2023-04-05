from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 10
count_attempt = 1
max_attempt = 5
rand_num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f'Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT} за {max_attempt} попыток.')
user_num = int(input('Введите число: '))
while user_num != rand_num and count_attempt != max_attempt:
    print('Больше' if user_num < rand_num else 'Меньше')
    user_num = int(input('Введите число: '))
    count_attempt += 1

if count_attempt == max_attempt:
    print(f'Вы не угадали число {rand_num}')
else:
    print(f'Поздравляю вы угадали число {rand_num} с попытки № {count_attempt}')
