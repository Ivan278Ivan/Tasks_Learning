numbers = numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Данные числа
primes = []  # Простые числа
notprimes = []  # Остальные числа
is_prime = True
for i in range(1, len(numbers)):
    is_prime = True
    for j in range(1, (numbers[i])):
        if numbers[i] % j == 0 and i != j and j != 1:
            is_prime = False
            break
    if is_prime == True:
            primes.append(numbers[i])
    if is_prime == False:
        notprimes.append(numbers[i])

print(primes)
print(notprimes)
