from Semana5 import ejemplos_if

print("--- Bienvenido al probador ---")

print("Seleccione que funcion quiere usar: ")
print("1. Menor que 0")

seleccion = int(input())

if seleccion == 1:
    frase = ejemplos_if.es_negativo(int(input("Ingrese su numero: ")))
    print(frase)
