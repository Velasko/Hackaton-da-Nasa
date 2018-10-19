# Os parametros para a funcao open 
# sao: o nome e como abrir o arquivo.
# parametros para abrir o arquivo:
# w -> write
# r -> read
# a -> append
# b -> fazer operacao em bytes
with open('arquivo.txt', 'w') as file:
	file.write('Ola mundo!')

with open('arquivo.txt', 'r') as file:
	lines = file.readlines()

for line in lines:
	print(line)