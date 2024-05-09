import numpy as np 
import scipy.linalg

# Questão 1:
# Considere os vetores:

# a
# [1] 11 11  7  7 10
# b
# [1]  4 15  9  6  8
# Calcule a subtração de a−b=c
# . Para incluir sua resposta faça a soma de c
# . A resposta deve ser um único valor numérico com até três casas decimais (se necessário).

a = np.array([11, 11,  7,  7, 10])
b = np.array([4, 15, 9, 6, 8])
c = a - b
print(sum(c))

# Questão 2:

# Use o método de Jacobi para resolver o sistema Ax=b onde A e b são dados abaixo. Quantas iterações foram necessárias para o método convergir? Use como valores iniciais um vetor de zeros. Sua resposta deve ser apenas um número inteiro.

# A
# #      [,1] [,2] [,3] [,4]
# # [1,]  2.5  0.8  0.8  0.7
# # [2,]  0.8  2.5  0.7  0.8
# # [3,]  0.8  0.7  2.5  0.8
# # [4,]  0.7  0.8  0.8  2.5
# b
# # [1]  9 11  4 10

A =  np.array([[2.5,  0.8,  0.8,  0.7],
               [0.8,  2.5,  0.7,  0.8],
               [0.8,  0.7,  2.5,  0.8],
               [0.7,  0.8,  0.8,  2.5]])

b = np.array([9, 11,  4, 10])

x = np.zeros(len(A[0]))

def jacobi(A, b, x, tol=1e-04, max_iter=100):

  n = len(b)
  x0 = x.copy()
  for it in range(max_iter):
    for i in range(n):
      soma = 0
      for j in range(n):
        if j != i:
          soma += A[i, j] * x[j]
      x[i] = (b[i] - soma) / A[i, i]

    if np.linalg.norm(x - x0) < tol:
      return x, it

  
  return x, max_iter


x, iteracoes = jacobi(A, b, x0)

print("Solução:", x)
print("Iterações:", iteracoes)

# Questão 3:

# Considere a decomposição LU da matrix A dada abaixo. O traço da matriz U é? Sua resposta deve ser um número. Use três casas decimais (se necessário).

# A
# ##     1   2   3   4
# ## 1 1.0 0.8 0.8 0.7
# ## 2 0.8 1.0 0.7 0.8
# ## 3 0.8 0.7 1.0 0.8
# ## 4 0.7 0.8 0.8 1.0

A = np.array([[1.0, 0.8, 0.8, 0.7],
              [0.8, 1.0, 0.7, 0.8],
              [0.8, 0.7, 1.0, 0.8],
              [0.7, 0.8, 0.8, 1.0]])

# Decomposição LU
P, L, U = scipy.linalg.lu(A)

# Imprimir as matrizes L e U
print("Matriz L:")
print(L)
print("\nMatriz U:")
print(U)

trace_U = np.trace(U)

# Imprimindo o traço da matriz U
print("Traço da matriz U:", trace_U)

# Questão 4 

# Considere as matrizes A e B conforme abaixo:

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]   14    9   14   18   10
# ## [2,]   10   14    7   15    6
# ## [3,]    5    5   13    9    9
# ## [4,]    4   13    7   11   12
# ## [5,]   15   10    9   15   17
# B
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]   15    8   11    9   13
# ## [2,]    6    9    8   16    9
# ## [3,]    9    8   12   14   14
# ## [4,]    7   10    9    7    7
# ## [5,]   10   11   10    8    5

# Calcule a matriz C=A+B. Para incluir a sua resposta some todos os elementos da matriz C. Sua resposta deve ser um único número. Use três casas decimais (se necessário).

A = np.array([[14,    9,   14,   18,   10],
              [10,   14,    7,   15,    6],
              [5,    5,   13,    9,    9],
              [4,   13,    7,   11,   12],
              [15,   10,    9,   15,   17]])

B = np.array([[15,    8,   11,    9,   13],
              [6,    9,    8,   16,    9],
              [9,    8,   12,   14,   14],
              [7,   10,    9,    7,    7],
              [10,   11,   10,    8,    5]])

C = A + B
print(np.sum(C))

# Questão 5:

# Considere as matrizes A e B conforme abaixo:

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]   14   21   10    9    8
# ## [2,]   10    7   11   10   10
# ## [3,]    8    6   12    7    7
# ## [4,]   12   10    8   12    9
# ## [5,]   14    8   10   12   11
# B
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]    8    6   12   12    5
# ## [2,]   12   12   13   13   10
# ## [3,]    8   12   18    9    7
# ## [4,]   11    9    2   10   13
# ## [5,]   10   14    9   14   13
# Calcule a matriz o produto entre as matrizes A e B. Coloque o resultado em uma nova matriz chamada de C. Para incluir a sua resposta some todos os elementos da matriz C
# . Sua resposta deve ser um único número. Use três casas decimais (se necessário).

A = np.array([[14,   21,   10,    9,    8],
              [10,    7,   11,   10,   10],
              [8,    6,   12,    7,    7],
              [12,   10,    8,   12,    9],
              [14,    8,   10,   12,   11]])

B = np.array([[8,    6,   12,   12,    5],
              [12,   12,   13,   13,   10],
              [8,   12,   18,    9,    7],
              [11,    9,    2,   10,   13],
              [10,   14,    9,   14,   13]])

C = A * B
print(np.sum(C))

# Questão 6:
# Considere os vetores:

# a
# ## [1] 12 11 10  8  6
# b
# ## [1] 12 14  5  9  8
# Calcule a soma de a+b=c. Para incluir sua resposta faça a soma de c. A resposta deve ser um único valor numérico com até três casas decimais (se necessário).

a = np.array([12, 11, 10,  8,  6])
b = np.array([12, 14,  5,  9,  8])
c = a + b
print(sum(c))

# Questão 7:
# Considere o vetores a e b:

# a
# ## [1] 11 10  8  8 13
# b
# ## [1] 12  9 13 10  6
# Calcule o produto interno de a por b, ou seja c=a⋅b. Para incluir sua resposta faça a soma de c. A resposta deve ser um único valor numérico com até três casas decimais (se necessário).

a = np.array([11, 10,  8,  8, 13])
b = np.array([12,  9, 13, 10,  6])
c = a * b
print(sum(c))

# Questão 8:

# Considere o escalar α e a matriz A conforme abaixo:

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]   13    9   12    2    5
# ## [2,]    6    8    6   19    5
# ## [3,]   13    9   11    7    9
# ## [4,]   13   15   11   10   10
# ## [5,]   13    5   11    8   13
# alpha
# ## [1] 3
# Calcule a matriz C=αA. Para incluir a sua resposta some todos os elementos da matriz C Sua resposta deve ser um único número. Use três casas decimais (se necessário).

A = np.array([[13,    9,   12,    2,    5],
              [6,    8,    6,   19,    5],
              [13,    9,   11,    7,    9],
              [13,   15,   11,   10,   10],
              [13,    5,   11,    8,  13]])

alpha = 3

C = A * alpha
print(np.sum(C))

# Questão 9:

# Obtenha os valores singulares da matriz A abaixo. Sua resposta deve ser quatro valores. Use três casas decimais (se necessário).

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]   10   10   12   10   16
# ## [2,]    9    8    9   11    9
# ## [3,]   14    8    7   10    3
# ## [4,]    7    7    7   10   10

A = np.array([[10,   10,   12,   10,   16],
              [9,    8,    9,   11,    9],
              [14,    8,    7,   10,    3],
              [13,   15,   11,   10,   10],
              [7,    7,    7,   10,   10]])

U, S, V = np.linalg.svd(A)
print("Valores singulares:")
print(S)

# Questão 10:

# Considere as matrizes A e B conforme abaixo:

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]    8    9    7    4   13
# ## [2,]   10    8    6   20   10
# ## [3,]   13   11    7   12    7
# ## [4,]    6   12    6    8    9
# ## [5,]   11    9   10    7    8
# B
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]    8   13   12   15    9
# ## [2,]   11    6    6   14    6
# ## [3,]    6    5   17   10   14
# ## [4,]   13    9   10   18   10
# ## [5,]   13   10   15   11    9
# Calcule a matriz o produto de Hadamard entre as matrizes A e B
# Coloque o resultado em uma nova matriz chamada de C
# Para incluir a sua resposta some todos os elementos da matriz C
# Sua resposta deve ser um único número. Use três casas decimais (se necessário).

A = np.array([[8,    9,    7,    4,   13],
              [10,    8,    6,   20,   10],
              [13,   11,    7,   12,    7],
              [6,   12,    6,    8,    9],
              [11,    9,   10,    7,    8]])

B = np.array([[8,   13,   12,   15,    9],
              [11,    6,    6,   14,    6],
              [6,    5,   17,   10,   14],
              [13,    9,   10,   18,   10],
              [13,   10,   15,   11,    9]])

C = A * B
print(np.sum(C))

# Questão 11:

# Obtenha os valores singulares da matriz A abaixo. Sua resposta deve ser quatro valores. Use três casas decimais (se necessário).

# A
# ##      [,1] [,2] [,3] [,4] [,5]
# ## [1,]    8    6   10    8    8
# ## [2,]   10    9    6   12   13
# ## [3,]    9    8    5   11   11
# ## [4,]    8    5    6    8    7

A = np.array([[8,    6,   10,    8,    8],
              [10,    9,    6,   12,   13],
              [9,    8,    5,   11,   11],
              [8,    5,    6,    8,    7]])

U, S, V = np.linalg.svd(A)
print("Valores singulares:")
print(S)

# Questão 12:

# Obtenha os autovalores da matriz A. Sua resposta deve ser quatro valores. Use três casas decimais (se necessário).

# A
# ##     1   2   3   4
# ## 1 2.0 1.6 1.6 1.6
# ## 2 1.6 2.0 1.6 1.6
# ## 3 1.6 1.6 2.0 1.6
# ## 4 1.6 1.6 1.6 2.0

A = np.array([
    [2.0, 1.6, 1.6, 1.6],
    [1.6, 2.0, 1.6, 1.6],
    [1.6, 1.6, 2.0, 1.6],
    [1.6, 1.6, 1.6, 2.0]
])

autovalores = np.linalg.eig(A)

print("Autovalores:", autovalores)

# Questão 13:

# Considere a decomposição LU da matrix A dada abaixo. O traço da matriz U é? Sua resposta deve ser um número. Use três casas decimais (se necessário).

# A
# ##     1   2   3   4
# ## 1 1.0 0.7 0.7 0.7
# ## 2 0.7 1.0 0.7 0.7
# ## 3 0.7 0.7 1.0 0.7
# ## 4 0.7 0.7 0.7 1.0

A = np.array([[1.0, 0.7, 0.7, 0.7],
              [0.7, 1.0, 0.7, 0.7],
              [0.7, 0.7, 1.0, 0.7],
              [0.7, 0.7, 0.7, 1.0]])

# Decomposição LU
P, L, U = scipy.linalg.lu(A)

# Imprimir as matrizes L e U
print("Matriz L:")
print(L)
print("\nMatriz U:")
print(U)

trace_U = np.trace(U)
print(trace_U)