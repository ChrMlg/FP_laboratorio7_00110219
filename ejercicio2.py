n=int(input("Cantidad de casos a evaluar: "))
i=0
while (i<n):    #ciclo que se repite segun cantidad de casos asignados
    i=i+1
    print("Caso ",i,": ")
    a=int(input("Primer numero: ")) #solicitud de valores
    b=int(input("Segundo numero: "))
    if a<b:     #menor
        print(a," es menor que ",b) 
    if a>b:     #mayor
        print(a," es mayor que ",b)
    if a==b:    #igual
        print(a," es igual a ",b)
        