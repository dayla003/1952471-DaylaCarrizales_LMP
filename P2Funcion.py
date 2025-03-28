def es_par(numero):
    if(numero % 2 == 0):
        return "Es par"
    else:
        return "Es impar"

num = int(input("Ingresa un número: "))
resultado = es_par(num)
print(resultado)