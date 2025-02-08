contador = 1
limite = 5

nombres = ["Ana", "Luis", "Carlos"]
edades = (15, 22, 30)

saldos = {
    "Ana": 50,
    "Luis": 200,
    "Carlos": 10
}

while contador <= limite:
    print(f"Contador: {contador}")
    contador += 1

for i in range(len(nombres)):
    nombre = nombres[i]
    edad = edades[i]
    saldo = saldos[nombre]

    if edad >= 18 and saldo >= 100:
        print(f"{nombre} puede realizar una compra")
    elif edad < 18:
        print(f"{nombre} es menor de edad")
    else:
        print(f"{nombre} no tiene suficiente saldo")