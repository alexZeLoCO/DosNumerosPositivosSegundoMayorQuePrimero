numero=0        #NUMERO
n = (int (input("Introduzca un valor positivo: ")))     #SOLICITA VALOR
string=""

while n<0:      #MIENTRAS NUMERO SEA NEGATIVO
    n = (int(input("Introduzca un valor positivo: ")))      #SOLICITA VALOR

while n/10>0:       #MIENTRAS HAYA DIGITO
    digito = n%2       #COGER SIGUIENTE CIFRA
    numero = numero*10+digito       #SUMAR CIFRA AL TOTAL
    n=n//2     #QUITAR CIFRA
    string=string+str(digito)

print (string)      #OUTPUT