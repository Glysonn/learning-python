print('**********************************')
print('Qual operação você quer fazer? \n')
choice = input(('1- SOMA\n2- SUBTRAÇÃO\n3- MULTIPLICAÇÃO\n4- DIVISÃO\n'))

#numX = int(input("Digite o número um: "))
#numY = int(input("Digite o número dois: "))
numY, numX = 5, 5


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
    return x/y


if choice == '1':
    print('Você escolheu soma')
#print(soma(numX, numY))
