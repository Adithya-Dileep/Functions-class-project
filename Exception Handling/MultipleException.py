try:
    age = int(input('Enter the age: '))
    print(age)
    a = 10 / 0
    print(a)
except ValueError as ve:
    print('Enter only numbers')
except ZeroDivisionError as z:
    print('Number cannot be divisible by 0')
else:
    print('No exceptions')
finally:
    print('Exception completed')