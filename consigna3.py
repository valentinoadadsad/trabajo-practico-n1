import numpy as np

M = np.array([
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
])

C = np.array([
    [30, 20, 10],
    [15, 25, 20],
    [40, 10, 30]
])

print("=== MATRIZ M ===")
print(M)

print("\n=== MATRIZ C ===")
print(C)

print("\n=== PROMEDIOS POR FUNCIÓN ===")

funciones = [
    "Autenticación",
    "Procesamiento",
    "Reportes"
]

promedios = np.mean(M, axis=1)

for i in range(len(funciones)):
    print(f"{funciones[i]}: {promedios[i]:.2f} ms")

print("\n=== TRANSPUESTA DE M ===")
print(M.T)

print("\n=== PRODUCTO MATRICIAL M · C ===")
producto = np.dot(M, C)
print(producto)

print("\n=== PRODUCTO DE HADAMARD ===")
hadamard = M * C
print(hadamard)

print("\n=== DETERMINANTE DE M ===")
determinante = np.linalg.det(M)
print(round(determinante))

print("\n=== ANÁLISIS ===")

mayor_promedio = max(promedios)
indice = np.argmax(promedios)

print(f"La función más costosa es: {funciones[indice]}")
print(f"Promedio: {mayor_promedio:.2f} ms")

promedios_servidores = np.mean(M, axis=0)

servidor = np.argmin(promedios_servidores) + 1

print(f"Servidor más eficiente: S{servidor}")
