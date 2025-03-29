#Función para encontrar el mayor de 3 números
def mayor_de_tres(a, b, c):
    if(a>b and a>c):
        return a
    
    if(b>a and b>c):
        return b
    
    if(c>a and c>b):
        return c

print(mayor_de_tres(5, 12, 7))  # Salida: 12


#Función que suma los elementos de una lista
def suma_lista(lista):
    total = 0
    for num in lista:
        total += num
    return total

print(suma_lista([1, 2, 3, 4]))


#Función que verifica si un número es par o impar
def es_par(numero):
    if(numero % 2 == 0):
        return True
    else:
        return False

print(es_par(4))
print(es_par(7))


#Función que cuenta las vocales en una cadena
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

print(contar_vocales("Hola Mundo"))


#Función que invierte una cadena (sin usar [::-1])
def invertir_cadena(cadena):
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

print(invertir_cadena("Python"))


#Función que devuelve el factorial de un número
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5))
