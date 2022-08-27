print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("Programa que calcula Hipotenusa de un Trinagula")

from math import sqrt

ladoA= float(input("Indique el valor de Langitud Largo:"))
ladoB= float(input("Indique el valor de Langitud Alto:"))

hipotenusa=sqrt(ladoA**2 + ladoB**2)
print ("El valor de la Hipotenusa es: ", hipotenusa)

              
