def soma(a, b):
    return f"Resultado: {a + b}"

def subtracao(a, b):
    return f"Resultado: {a - b}"

def multiplicacao(a, b):
    return f"Resultado: {a * b}"

def divisao(a, b):
    return f"Resultado: {a / b}"

def resto(a, b):
    return f"Resultado: {a % b}"

print("### Calculadora Simples ###")

print("\nEscolha as Operações:\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Resto\n0- Sair\n")
escolhaOp = int(input("Resultado da escolha: "))

while escolhaOp != 0:
    if escolhaOp > 0 and escolhaOp < 6:
        if escolhaOp == 1:
            num1 = float(input("\nInforme o primeiro valor: "))
            num2 = float(input("Informe o segundo valor: "))
            print(soma(num1, num2))
        elif escolhaOp == 2:
            num1 = float(input("\nInforme o primeiro valor: "))
            num2 = float(input("Informe o segundo valor: "))
            print(subtracao(num1, num2))
        elif escolhaOp == 3:
            num1 = float(input("\nInforme o primeiro valor: "))
            num2 = float(input("Informe o segundo valor: "))
            print(multiplicacao(num1, num2))
        elif escolhaOp == 4:
            num1 = float(input("\nInforme o primeiro valor: "))
            num2 = float(input("Informe o segundo valor: "))
            print(divisao(num1, num2))
        elif escolhaOp == 5:
            num1 = float(input("\nInforme o primeiro valor: "))
            num2 = float(input("Informe o segundo valor: "))
            print(resto(num1, num2))
    else:
        print("Escolha incorreta!\n")
    escolhaOp = int(input("\nResultado da escolha: "))