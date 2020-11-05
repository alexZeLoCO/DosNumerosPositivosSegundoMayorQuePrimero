n = int (input("Introduzca el primer número: "))
if n<0:
    while n<0:
        print(n)
        n = int (input ("Introduzca un nuevo número: "))
else:
    print ("El primer número ya era positivo.")