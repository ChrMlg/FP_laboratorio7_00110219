
def primus(x): #funcion que determina si un numero es primo 
        i=1
        while i<x-1:
            i=i+1
            sob=x%i
    
            if (sob==0):
                return "" #retorna un valor "vacio" si el numero evaluado no es primo
            if (i==x-1):
                return x    #retorna solo numero primos

x=int (input("Digite inicio de rango: "))   #solicitud de valores 
y=int (input("Digite final de rango: "))
aux=x-1
while(aux<y): #ciclo que se repite mientras se evalua si los numeros dentro de un rango son primos o no 
    aux=aux+1
    ret=primus(aux)
    if (aux==x): #impresion unica dentro de un ciclo
        print ("Los numero primos en el rango indicado son:")
    print (ret,end=" ") #imprime todos los numeros primos dentro del rango asignado