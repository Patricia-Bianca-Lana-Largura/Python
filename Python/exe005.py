a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

# Uso de Condicional if, o final da condição é definida pela própria identação do código.
# elif é um else com if.
if a >= b and a >= c:
    print('O maior número é {}'.format(a))
elif b >= a and b >= c:
    print('O maior número é {}'.format(b))
else:
    print('O maior número é  {}'.format(c))


resto_a = a % 2
resto_b = b % 2
resto_c = c % 2
if resto_a == 0 or resto_b == 0 or resto_c == 0:
    print('\nFoi digitado um número par!')
else:
    print('\nNenhum número par foi digitado!')
print('\nFinal do programa!')
