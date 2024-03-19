a = float(input('Qual o valor de a? '))
b = float(input('Qual o valor de b? '))
c = float(input('Qual o valor de c? '))

delta = b**2 - 4*a*c
raiz = delta**0.5

x1 = (-b + raiz) / (2*a)
x2 = (-b - raiz) / (2*a)

print('Delta:',delta)
print('Raiz:',raiz)
print('O valor de X1:',x1)
print('o valor de X2:', x2)