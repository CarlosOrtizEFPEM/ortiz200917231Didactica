import time
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("\nMuestra vocales en un texto")

texto = input("Ingrese un texto: ")

contador = 0
vocales = set("aeiouAEIOU") 
for texto in texto: 
    if texto in vocales: 
        contador = contador + 1
print("No. de Vocales es :", contador)

print("\nSalir del programa")
print(quit())         
#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
