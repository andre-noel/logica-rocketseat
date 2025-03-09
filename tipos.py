## Tipos primitivos

# - int: números inteiros
# - float: números decimais
# - str: cadeias de caracteres
# - bool: valores lógicos (True ou False)

# Exemplo de uso de tipos primitivos
a = 5
b = 3.14
c = 'Python'
d = True

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Operações aritméticas
a = 5
b = 3
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto = a % b
potencia = a ** b

print('Soma:', soma)
print('Subtração:', subtracao)
print('Multiplicação:', multiplicacao)
print('Divisão:', divisao)
print('Divisão inteira:', divisao_inteira)
print('Resto:', resto)
print('Potência:', potencia)

# Operações com strings
a = 'Python'
b = ' é uma linguagem de programação'
c = a + b
d = a * 3

print(c)
print(d)

# Operações com booleanos

a = True
b = False

print('a and b:', a and b)
print('a or b:', a or b)
print('not a:', not a)

# Conversão de tipos

a = 5
b = '3.14'
c = '5'
d = 'True'

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

b = float(b)
c = int(c)
d = bool(d)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
