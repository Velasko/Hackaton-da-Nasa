
x = (0, 1, 2, 3, 4)
y = [0, 1, 2, 3, 4]
z = range(5)

print('x eh tipo:', type(x) )

print('y eh tipo:', type(y) )

print('z eh tipo:', type(z) )

print('3o item de x:', x[2])

print('ultimo item de x:', x[-1])

#x nao suporta a seguinte operacao, por ser uma tupla
#entretanto, y eh uma lista, entao aceita
y[2] = 7
print(y)

#pegando uma seccao do array
print( x[1: 3] )

#pegando a cada dois caracteres
print( x[::2] )

#invertendo a ordem
print( x[::-1] )

#cuidado ao atribuir uma lista a outra variavel!
a = y
a.append(3)
print('a:', a)
print('y:', y)

a = y[:]
a.append(3)
print('a:', a)
print('y:', y)

print("max(y) =", max(y))
