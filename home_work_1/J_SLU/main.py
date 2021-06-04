import numpy as np
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())


A = np.array([[a, b],[c, d]])
B = np.array([e, f])

C = np.array([[a, b, e],[c, d, f]])

"""
По теореме Кронекера-Капелли система линейных уравнений имеет бесконечно много решений, если 
1) определитель системы равен нулю, и 
2) ранг расширенной матрицы системы равен рангу матрицы системы.
"""

if np.linalg.det(A) == 0 and np.linalg.matrix_rank(A) == np.linalg.matrix_rank(C):
    print('Бесконечно много решений')
else:
    X = np.linalg.solve(A, B)
    print(2, X[0], X[1])