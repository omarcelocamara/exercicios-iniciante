#Olá Mundo:

print('Olá, Mundo!')
###########################################

#Pedir um número e mostrar na tela qual foi:

n = float(input('Digite um número: '))
print(f'O número escolhido foi: {n}')
############################################

#Printar a soma entre dois números:

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} é: {s}')
###############################################

#Programa que pede 4 notas e faz a média:

n1 = float(input('Qual foi a sua nota no primeiro bimestre? '))
n2 = float(input('Qual foi a sua nota no segundo trimestre? '))
n3 = float(input('Qual foi a sua nota no terceiro trimestre? '))
n4 = float(input('Qual foi a sua nota no quarto trimestre? '))

soma =  n1 + n2 + n3 + n4
media = soma/4

print(f'A sua média anual foi: {media}!')
##################################################

#Programa que converte metros para centimetros:

n = float(input('Digite uma medida em metros: '))
converte = n*100
print(f'{n} metros são {converte}cm')
####################################################

#Pede o raio e mostra a área de um círculo - A = pi r²

r = float(input('Digite o raio do círculo: '))
calcular = 3.14*r**2
print(f'A área de um círculo cujo o raio vale {r} é {calcular}')
####################################################

#Programa que calcula a área de um quadrado e mostra o dobro da área:

l = float(input('Qual é o lado desse quadrado? '))
area = l*l
area_dobro = area*2
print(f'A área deste quadrado é {area} e o dobro dela é {area_dobro}')
####################################################

#Programa que pergunta quanto ganha por hora e o número de horas trabalhadas no mês. Calcular o total do salário mensal:

valor_hora = float(input('Quanto você ganha por hora trabalhada? '))
horas_trabalhadas = float(input('Quantas horas você trabalha no mês? '))
calculo = valor_hora*horas_trabalhadas
print(f'O seu salário referido no mês é de R${calculo}') 
####################################################

#Programa que peça temperatura em graus Fahrenheit e mostra em graus Celsius [C = 5*((F-32)/9)]:

while True:#só pra repetir sozinho o programa pra testar
    gf = float(input('Digite o valor da temperatura em graus Fahrenheit: '))
    c = 5*(gf-32)/9

    print(f'A temperatura em Celsius é: {c}')
    break
####################################################

#Programa que peça temperatura em graus Fahrenheit e mostra em graus Celsius usando função: 

def calcular(gf):
      c = 5*(gf-32)/9
      print(f'O valor em Celsius é: {c}')


gf = float(input('Digite o valor da temperatura em graus Fahrenheit: '))
calcular(gf)
####################################################

#Programa que pede a temperatura em graus Celsius e transoforma em Fahrenheit: (C*1,8+32)

def calcular(c):
  f = c*1.8+32
  print(f'A temperaatura em fahrenheit é: {f}')

while True:
  c = float(input('Digite a temperatura em graus Celsius: '))
  calcular(c)
  break
 ###################################################

#Programa que pede 2 número inteiros e um número real, calcular e mostrar: a)o produto do dobro do primeiro com a metade do segundo. b)a soma do triplo do primeiro com o terceiro. c)o terceiro elevado ao cubo.

def calcular(ni1, ni2, nr):
  a = (ni1*2)*(ni2/2)
  b = (ni1*3)+nr
  c = nr**3

  print(f'O resultado da questão a é: {a}, o resultado da questão b é: {b}, o resultado da questão c é {c}.')

ni1 = int(input('Digite um número inteiro: '))
ni2 = int(input('Digite outro número inteiro: '))
nr = float(input('Digite um número real: '))
calcular(ni1, ni2, nr)
####################################################

#Tendo como dados a altura de uma pessoa, construir um algorítimo que calcule o seu peso ideal, usando a seguinte fórmula: (72.7*altura)-58

def calcular(h):
  peso_ideal = (72.7*h)-58
  print('O seu peso ideal é aproximadamente:',int(peso_ideal),'kg')

h = float(input('Qual é a sua altura? '))
calcular(h)
####################################################

#Tendo como dados a altura de uma pessoa, construir um algorítimo que calcule o seu peso ideal, usando a seguinte fórmula: a)(72.7*altura)-58 para homens, b) (62.1*h) - 44.7 para mulheres.

def calcular(h):
  peso_ideal_homem = int((72.7*h)-58)
  peso_ideal_mulher = int((62.1*h) - 44.7)

  print(f'O seu peso ideal é {peso_ideal_homem}kg, caso você seja homem, caso contrário, é {peso_ideal_mulher}kg')

h = float(input('Qual é a sua altura?'))
calcular(h)
####################################################

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

def calcular(peso):
  exc = peso - 50
  multa = exc*4
  if(exc >= 1):
    print(f'O excedente de peso foi de {exc}kg e a multa a pagar é R${multa}')
  else:
    print('Você não ultrapassou o limite de kg hoje! Portanto, não há multa.')

peso = float(input('Quanto em kg você trouxe de peso hoje?'))
calcular(peso)
####################################################

# Programa que pergunta quanto você ganha por hora e o número de horas trabalhadas no mês. Calcular o total do salário referido no mês, sabendo que são descontados 11% para o imposto de renda, 8% para o INSS e 5% para o sindicato, o programa deve dar: a)salário bruto, b)quanto pagou ao INSS, c)Quanto pagou ao sindicato, d)O salário líquido, e)Cálculo dos descontos e o salário líquido.

def calcular(valor_hora,horas_mes):
  bruto = valor_hora*horas_mes
  ir = bruto * (11/100)
  inss = bruto*(8/100)
  sin = bruto*(5/100)
  liq = bruto-ir-inss-sin
  print('Nota Salarial:')
  print(f'Bruto: R${bruto}')
  print(f'INSS: -R${inss}')
  print(f'IR: -R${ir}')
  print(f'Sindicato: -R${sin}')
  print(f'Salário Líquido: R${liq}')

valor_hora = float(input('Quanto você ganha por hora trabalhada?'))
horas_mes = float(input('Quantas horas você trabalha no mês?'))
calcular(valor_hora, horas_mes)
####################################################

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

def calcular(tam):
  litro = tam/3
  lata = 18
  x = int(litro/lata)
  price = x*80
  print(f'Você precisará de {x} latas para pintar {tam}m², o que custará um total de: R${price}')

tam = float(input('Qual é o tamanho em m² da área que deve ser pintada?: '))
calcular(tam)
####################################################

# Programa para a loja de tintas que pede o tamanho em metros quadrados da área a ser pintada. 1 litro para cada 6 metros quadrados. Latas de 18 litros custam 80 reais, ou galões de 3.6 litros custam 25 reais. Informar o usuário as quantidades de tinta a serem compradas e os preços em 3 situações: 1) Comprar apenas latas de 18 litros. 2)Comprar apenas galões de 3.6 litros. 

def calcular(tam,resposta):
  litro = tam/6
  lata = 18 #80reais
  gal = 3.6 #25reais
  xlata = litro/lata #quantas latas
  xgal = litro/gal #quantos galões
  price_lata = int(xlata*80)
  price_gal = int(xgal*80)
 

  if(resposta == 1):
      print(f'Para pintar {tam}m², você precisará de {litro} litros de tinta, o que custará: R${price_lata}')
  elif(resposta == 2):
      print(f'Para pintar {tam}m², você precisará de {litro} litros de tinta, o que custará: R${price_gal}')

tam = float(input('Qual é o tamanho em m² da área a ser pintada?: '))
while True:
  resposta = int(input('De que forma você prefere comprar a tinta? [1]: Apenas latas de 18 litros. [2]: Apenas galões de 3.6 litros.'))
  calcular(tam, resposta)
  break
####################################################

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam = float(input('Qual é o tamanho do arquivo em MBs?: '))
v = float(input('Qual é a velocidade do link de internet eem Mbps?: '))
seg = tam/v
min = int(seg/60)
seg = seg%60
print(f'Tempo aproximado para download: {min} minutos e {seg} segundos.')
####################################################