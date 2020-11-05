n = int (input("Introduzca el primer número: "))
suma=0
contador = 0
if n>=0:
    while n>=0:
        contador = contador+1
        suma=suma+n
        n = int (input ("Introduzca un nuevo número: "))
else:
    print ("El primer número ya era negativo.")
print("La media aritmética es igual a:",suma/contador)