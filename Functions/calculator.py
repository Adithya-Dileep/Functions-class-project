def add(a, b):
    return a+b 
def sub(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b
print('Select your choice of operation')
print('1.Add')
print('2.Sub')
print('3.Multiply')
print('4.Divide')
choice = input('Enter the choice')
num1 = int(input('Enter the first number'))
num2 = int(input('Enter the second number'))
if choice == '1':
    print('Result', add(num1, num2))
elif  choice == '2':
    print('Result', sub(num1, num2))
elif  choice == '3':
    print('Result', multiply(num1, num2))
elif  choice == '4':
    print('Result', divide(num1, num2))
else:
    print('Invaild input')