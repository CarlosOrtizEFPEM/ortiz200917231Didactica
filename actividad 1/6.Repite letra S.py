import time
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("\nMuestra letra quese repite en texto")

letra=input("Ingrese letra: ")
evaluar=input("Ingrese texto a evaluar: ")

print ("No. veces que aparece letra" , letra, " son: ",evaluar.count(letra))

print("\nSalir del programa")
print(quit())
           
#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
