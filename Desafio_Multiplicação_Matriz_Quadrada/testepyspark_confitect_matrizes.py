# -*- coding: utf-8 -*-
"""TESTEPYSPARK_Confitect_Matrizez.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iVuBNNCkDnMbPOI2shjNH0bXe8De6IUN

## Intalando a Biblioteca principal, caso ela já não esteja disponível no ambiente
"""

!pip install numpy

"""## Importando apenas as funções que serão necessárias"""

from numpy import random, dot, array, reshape
from math import sqrt

"""## Esta primeira função está programada para fazer o produto de Matriz Quadrada entre Matrizes Idênticas, que foram geradas através de números aleatórios

É necessário passar para ela, em sua chamada, o número mínimo e máximo do intervalo de onde serão gerados os números aleatórios, bem como o tamanho que se espera dessas Matrizes.

"""

def multiplica_matrizes_iguais(de, ate, n):
  if isinstance(de, int) and isinstance(ate, int) and isinstance(n, int) and de>=0 and ate > de and n>=0:
    x = random.randint(de,ate, (n,n))
    a = x
    b = x
    produto = dot(x,x)
    print('\n A e B são matrizes {}x{}'.format(n,n))
    print('A=\n{}\n'.format(a))
    print('B=\n{}\n'.format(b))
    print('Product=\n{}'.format(produto))
    return '\n Produto Matriz Quadrada, entre matrizes idênticas, Realizado com Sucesso'
  else:
    return "\n Apenas Números Inteiros e positivos serão aceitos"

"""## Já esta segunda função calcula o Produto de Matriz Quadrada entre Matrizes diferentes, que também foram geradas a partir de números aleatórios

Também é necessário passar para ela, em sua chamada, o número mínimo e máximo do intervalo de onde serão gerados os números aleatórios, bem como o número de colunas da primeira Matriz e de linhas da segunda.
Lembrando que o produto de Matriz Quadrada só é possível quando o número de colunas da primeira Matriz é igual ao número de linhas da segunda.
"""

def multiplica_matrizes_diferentes(de, ate, n):
  if isinstance(de, int) and isinstance(ate, int) and isinstance(n, int) and de>=0 and ate > de and n>=0:
    if n == 0:
      n = n+1
    if de > n:
      i = de
      de = n
      n = i
    m1 = random.randint(de,n) 
    m2 = random.randint(de,n)
    print('\nA é uma matriz {}x{}'.format(m1,n))
    print('\nB é uma matriz {}x{}\n'.format(n,m2))
    a = random.randint(de,ate, (m1,n))
    b = random.randint(de,ate, (n,m2))
    produto = dot(a,b)
    print('A=\n{}\n'.format(a))
    print('B=\n{}\n'.format(b))
    print('Product=\n{}'.format(produto))
    return '\n Produto Matriz Quadrada, entre matrizes diferentes, Realizado com Sucesso'
  else:
    return "\n O segundo número precisa ser maior do que o primeiro e apenas números inteiros e positivos serão aceitos"

"""## Já esta terceira função tem por objetivo chamar uma das duas outras funções caso o usuário queira trabalhar com valores aleatórios ou, também, fornecer o cálculo entre matrizes idênticas em que o próprio usuário pode colocar os elementos que deseja usar no produto."""

def calcula_matriz_quadrada():

  print("Você gostaria de fazer esse cálculo para matrizes iguais ou diferentes?\n")
  tipoMatriz = int(input('Digite 1 para Matrizes idênticas e 2 para Matrizes Diferentes: '))

  if tipoMatriz == 1:
    print('\nVocê gostaria de passar os elementos da Matriz para o cálculo?\n')
    tipoCalculo = int(input('Digite 1 para passar um intervalo com cada um dos elementos e 2 para que sejam elementos aleatórios: '))
    if tipoCalculo == 2:
      de = int(input('\n Digite o limite mínimo do intervalo: '))
      ate = int(input('\n Digite o limite máximo do intervalo: '))
      n = int(input('\n Digite o número de linhas e colunas, um único número: '))
      return multiplica_matrizes_iguais(de, ate, n)
    elif tipoCalculo == 1:
      sequencia = array(list(map(int, input("\n Digite os elementos numéricos e separados por vírgula: ").split(","))))
      size = sqrt(len(sequencia))
      try:
        matriz = sequencia.reshape(int(size), int(size))
        print('A=\n{}\n'.format(matriz))
        print('B=\n{}\n'.format(matriz))
        print('Product=')
        return dot(matriz,matriz)
      except ValueError:
        return "\n O Número de elementos não é suficiente para o cálculo de matriz quadrada"
  if tipoMatriz == 2:
    de = int(input('\nDigite o limite mínimo do intervalo: '))
    ate = int(input('\nDigite o limite máximo do intervalo: '))
    n = int(input('\nDigite o número de colunas de A e linhas de B, um único número: '))
    return multiplica_matrizes_diferentes(de, ate, n)

calcula_matriz_quadrada()

calcula_matriz_quadrada()

calcula_matriz_quadrada()

# def multiplica_matrizes_identicas(*elements):
#     size = sqrt(len(elements))
#     if size.is_integer():
#       matriz = array(elements).reshape(int(size), int(size))
#       # matriz = elements.reshape(int(size), int(size))
#       print('A=\n{}\n'.format(matriz))
#       print('B=\n{}\n'.format(matriz))
#       print('Product=')
#       return dot(matriz,matriz)
#     else:
#       raise RuntimeError("Número de elementos não é suficiente para o cálculo de matriz quadrada")