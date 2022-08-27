print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("Programa que indica el numero mayor de 3 valores")

# Vamos a poner los números en una lista
numeros = []

# Le agregamos 3 números
for i in range(3):
  numero = float(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)

# Asumir que el mayor es el primero de la lista
mayor = numeros[0]
# Recorrer y comparar
for numero in numeros:
    if numero > mayor:
        mayor = numero
# Imprimir el resultado
print("Mayor:", mayor)
