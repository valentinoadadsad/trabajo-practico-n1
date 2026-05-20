import matplotlib.pyplot as plt

def plan_a(x):
    return 40 * x + 200

def plan_b(x):
    return 70 * x + 50

def plan_c(x):
    return -2 * (x ** 2) + 80 * x + 100

horas = [0, 5, 10, 15, 20, 25, 30, 40, 50]

print("=== COSTOS DE LOS PLANES ===\n")

for x in horas:
    a = plan_a(x)
    b = plan_b(x)
    c = plan_c(x)

    print(f"Horas: {x}")
    print(f"Plan A: ${a}")
    print(f"Plan B: ${b}")
    print(f"Plan C: ${c}")

    menor = min(a, b, c)

    if menor == a:
        print("Más económico: Plan A")
    elif menor == b:
        print("Más económico: Plan B")
    else:
        print("Más económico: Plan C")

    print()

x_valores = list(range(0, 51))

y_a = [plan_a(x) for x in x_valores]
y_b = [plan_b(x) for x in x_valores]
y_c = [plan_c(x) for x in x_valores]

plt.plot(x_valores, y_a, label="Plan A")
plt.plot(x_valores, y_b, label="Plan B")
plt.plot(x_valores, y_c, label="Plan C")

plt.xlabel("Horas")
plt.ylabel("Costo")
plt.title("Comparación de planes")
plt.legend()
plt.grid(True)

plt.show()
