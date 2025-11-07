try:
    age = int(input('Enter the age: '))
except ValueError as ve:
    print('Enter only numbers')