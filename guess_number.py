from random import randint

number = randint(1, 100)
print('Euflfqnt xbckj jn 1 lj 100')

while True:
    guess = int(input('Введите число: '))
    
    if guess < number:
        print('Ваше число меньше того, что загадано.')
    
    if guess > number:
        print('Ваше число больше того, что загадано.')

    if guess == number:
        break

print('Отличная интуиция! Вы угадали число :)')