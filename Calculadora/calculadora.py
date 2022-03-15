numX = int(input("Digite o número um: "))
numY = int(input("Digite o número dois: "))


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


print(soma(numX, numY))
