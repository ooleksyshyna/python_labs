#9 розкладання чотирицифрового цілого числа і виведення на екран суми цифр у числі
number = int(input('Number:'))

a = int(number/1000)
b = int(number/100)%10
c = int(number/10)%10
d = number%10

print(f'{a} + {b} + {c} + {d} = {a + b + c + d}')
