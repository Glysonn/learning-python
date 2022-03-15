print('**********************************')
print('Qual operação você quer fazer? \n')
choice = input(('1- SOMA\n2- SUBTRAÇÃO\n3- MULTIPLICAÇÃO\n4- DIVISÃO\n'))
numX = float(input("Digite o número um: "))
numY = float(input("Digite o número dois: "))


def soma(x, y):
    x, y = numX, numY
    return x+y


def minus(x, y):
    x, y = numX, numY
    return x-y


def multiplicacao(x, y):
    x, y = numX, numY
    return x*y


def div(x, y):
    x, y = numX, numY
    if y < 0:
        print("Impossível dividir por zero!")
    return x/y


if choice == '1':
    print("Seu resultado é: ", soma(numX, numY))
elif choice == '2':
    print("Seu resultado é: ", minus(numX, numY))
elif choice == '3':
    print("Seu resultado é: ", multiplicacao(numX, numY))
elif choice == '4':
    print("Seu resultado é: ", div(numX, numY))
else:
    print("A operação que você escolheu é inválida!")
