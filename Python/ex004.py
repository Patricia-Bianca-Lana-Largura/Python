a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# Primeiro exemplo:
print('Soma: ', soma)
print('subtração: ', subtracao)
print('Multiplicação', multiplicacao)
print('Divisão: ', int(divisao))
print('Resto: ', int(resto))

# Segundo exemplo:
print(
    '\n Soma: {som}.'
    '\n Subtração: {sub}.'
    '\n Multiplicação: {mult}.'
    '\n Divisão: {div}.'
    '\n Resto: {rest}\n'
        .format(som=soma,
                sub=subtracao,
                mult=multiplicacao,
                div=divisao,
                rest=resto)
)

# Exemplo para conversão de unidades: print('soma: ' + str(soma)) Ele vai converter o tipo int para uma string para
# poder concatenar 2 valores do tipo string, o + só vai concatenar valores que são do mesmo tipo.

# No exemplo acima foi utilizado vírgula, mas se fosse utilizado o + seria necessário converter o tipo do valor.
