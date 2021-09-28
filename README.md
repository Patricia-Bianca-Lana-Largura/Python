# Phyton


### Comando `print` escreve algo na tela:

```
print ('Olá, Mundo')
print (7 + 4)
print ('7' + '4')
```
> No caso da terceira linha ele vai concatenar as 2 informações 7 e 4 tornando 74.

- **Variáveis**: assume qualquer um de um conjunto de valores.
> Toda a variável é um objeto dentro do Phyton.

```
nome = 'Patricia'   // tipo char
idade = 21            // tipo number
peso = 51,2         // tipo foat
print (nome, idade, peso)
```
> A utilização de vírgulas nesse caso concatena que nem o + logo acima, mas o uso da vírgula é importante quando os dados a serem concatenados são de tipos diferentes.

### Utilizando `input` para guardar valores dentro de variáveis:

```
nome = input ('Qual o seu nome? ')
idade = input ('Quantos anos você tem? ')
peso = input ('Quanto você pesa? ')

print (nome, idade, peso)
```

### Interpolação de valores:

```
dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')

print ('Você nasceu no dia', dia, 'de', str(mes), 'de', ano)

print ('Você nasceu no dia {DIA} de {MES} de {ANO}'.format(DIA=dia, MES=mes, ANO=ano))

print ('Você nasceu no dia {} de {} de {}'.format(dia,mes,ano))

# Utilizando alguns exemplos de interpolação.

```
```
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
```

#### Site do Curso:

[Curso em Vídeo]('https://www.cursoemvideo.com/')

[Digital Innovation One - Curso de Introdução à Programação com Python]('https://web.digitalinnovation.one/home')

#### Referências:

[JournalDev]('https://www.journaldev.com/23642/python-concatenate-string-and-int')

[eXcript]('http://excript.com/python/introducao-as-string-python.html')

