print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("Programa que calculo X valores")


n=int(input("ingrese numero de valores a promediar:"))
suma=0
i=1
while (i<=n):
    print ("ingrese el valor:",i)
    nota =float(input())
    suma=suma+nota
    i+=1
prom=suma/n
print("el promedio de notas es", prom)
