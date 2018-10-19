
def primeira_funcao():
	print('Ola, sou a primeira funcao!')


def segunda_funcao(x):
	return( x * 2 )

def terceira_funcao(x='Mundo'):
	print("Ola,", x, ', eu sou a terceira_funcao!')

def is_prime(x):
	'''Uma funcao que recebe um entrada x 
	retorna um boleano dizendo se x eh primo ou nao.'''
	for n in range(2, x):
		if x % n == 0:
			print(x, 'eh divisivel por', n)
			return False

	return True

def my_generator(x):
	y = 0
	while True:
		y += 1
		yield x * y

f = lambda x: x**2 + x + 2

#As funções, diferente de antes, devem ser chamadas
#para serem executadas

primeira_funcao()

#Sempre se usa o parenteses para chamar uma funcao

x = segunda_funcao(4)

print('x: ', x)

#Podemos renomear uma funcao usando a atribuicao:

primo = is_prime

print('primo(7):', primo(7))