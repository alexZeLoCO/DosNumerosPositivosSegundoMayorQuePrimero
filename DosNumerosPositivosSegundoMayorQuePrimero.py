n1 = (int)(input("Introduzca un número: "))     #PEDIR VALOR
n2 = (int)(input("Introdzca un  númerO: "))     #PEDIR VALOR

while (n1<0 or n2<0 or n2<n1):        #MIENTRAS NO SE CUMPLAN UNA DE LAS CONDICIONES
    n1 = (int)(input("Introduzca un número: "))     #PEDIR VALOR
    n2 = (int)(input("Introdzca un  númerO: "))     #PEDIR VALOR

print("Los números introducidos son:",n1,n2)        #OUTPUT

#EQUIVALENTE:
#WHILE (NOT(N1>=0 AND N2>=0 AND N2>N1)):
    #PEDIR VALORES