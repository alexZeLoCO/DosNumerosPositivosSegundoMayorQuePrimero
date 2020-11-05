n = int (input("Introduzca el primer número: "))
sumapares=0
contadorpares = 0
sumaimpares=0
contadorimpares=0
if n>=0:
    while n>=0:
        if (n%2==0):
            contadorpares=contadorpares+1
            sumapares=sumapares+n
        else:
            contadorimpares=contadorimpares+1
            sumaimpares=sumaimpares+n
        n = int (input ("Introduzca un nuevo número: "))
else:
    print ("El primer número ya era negativo.")
print("La media aritmética de los pares es igual a:",sumapares/contadorpares)
print("La media aritmética de los impares es igual a:",sumaimpares/contadorimpares)