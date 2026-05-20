sA = {101, 102, 103, 104, 105, 106}
sB = {104, 105, 106, 107, 108}
sC = {102, 105, 109}

print("=== OPERACIONES CON CONJUNTOS ===")

print("A ∩ B:", sA & sB)
print("A ∪ B:", sA | sB)
print("(A ∪ B) - C:", (sA | sB) - sC)
print("A Δ B:", sA ^ sB)

interseccion = {u for u in sA if u in sB}
sin_errores = {u for u in (sA | sB) if u not in sC}

print("\nComprensión de conjuntos:")
print("Intersección:", interseccion)
print("Sin errores:", sin_errores)

print("\nUsuarios en C pero no en A ∪ B:")
print(sC - (sA | sB))

print("\n=== LÓGICA PROPOSICIONAL ===")

def es_critico(usuario):
    p = usuario in sA
    q = usuario in sB
    r = usuario in sC
    return (p or q) and r

usuarios = sA | sB | sC

for usuario in sorted(usuarios):
    if es_critico(usuario):
        print(f"Usuario {usuario}: CRÍTICO")
    else:
        print(f"Usuario {usuario}: NO CRÍTICO")
