import numpy as np

# Sua lista original com strings
minha_lista = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
]

# Converte a lista em uma matriz NumPy de strings
matriz_numpy = np.array(minha_lista, dtype=str)

# Gira a matriz 90 graus no sentido anti-horário
matriz_girada = np.rot90(matriz_numpy)

# Imprime a matriz original
print("Matriz Original:")
print(matriz_numpy)

# Imprime a matriz girada
print("\nMatriz Girada:")
print(matriz_girada)

# Modifica uma string na posição (1, 1) da matriz girada
matriz_girada[1, 1] = 'MODIFICADO'

# Imprime a matriz girada com a string modificada
print("\nMatriz Girada com String Modificada:")
print(matriz_girada)
