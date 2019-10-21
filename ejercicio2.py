n=int(input("Cantidad de casos a evaluar: "))
i=0
while (i<n):
    i=i+1
    print("Caso ",i,": ")
    a=int(input("Primer numero: "))
    b=int(input("Segundo numero: "))
    if a<b:
        print(a," es menor que ",b)
    if a>b:
        print(a," es mayor que ",b)
    if a==b:
        print(a," es igual a ",b)
        