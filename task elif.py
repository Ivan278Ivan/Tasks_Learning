first = int(input('Введите число '))
second = int(input('Введите число '))
third = int(input('Введите число '))

if first == second and second == third:
    print('Равны три числа')
elif second == first or second == third or first == third:
    print('Равны два числа')
else:
    print('равных чисел нет')
