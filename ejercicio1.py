import math

print("//Numero de casos de prueba")
x=int(input("//Inicio de rango 1 "))
y=int(input("//Fin de rango 1 "))
a=int(input("//Inicio de rango 2 "))
b=int(input("//Fin de rango 2 "))

auxx=x
 p=x
 q=0
 r=0
tot1=0
if x%2==0:
    while auxx<y:
        auxx=auxx+2
        r=p+q
        q=r+p
        p=r

        
print (tot1-auxx2)


