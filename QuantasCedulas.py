moedas = [200, 100, 50, 10, 5, 2, 1]

conta = float(input('Valor da conta:'))
pago = float(input('Quanto você vai pagar?'))

troco = (pago - conta)

print(f'O valor do troco é {troco}.')

n200 = troco // 200 #divisão inteira.
print(f'Notas de 200: {n200}')
troco = troco - 200 * n200 #troco % 200 resto da divisão por 200
print(f'Notas de 200: {troco}')
n100 = troco // 100
troco = troco - n100 * 100
print(f'Notas de 100: {n100}')
n50 = troco // 50
troco = troco - n50 * 50
print(f'Notas de 50: {n50}')
n20 = troco // 20
troco = troco - n20 * 20
print(f'Notas de 20: {n20}')
n10 = troco // 10
troco = troco - n10 * 10
print(f'Nota de 10: {n10}')
