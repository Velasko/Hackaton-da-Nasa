
#enquanto verdade:
#	faça isso
y = 0
while True:
	print(y)
	y += 1

print('Iniciando o while:')
y = 0
while y < 10:
	print(y)
	y += 1
print('Final do while!')

print('Iniciando o for:')
for y in range(10):
	print(y)
print('Final do for!')

for caractere in 'Ola, mundo!':
	print(caractere)

for n, c in enumerate('Ola, mundo!'):
	if n == 3:
		continue
	print(c)