num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-': 
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
else:
    print("Operação inválida")