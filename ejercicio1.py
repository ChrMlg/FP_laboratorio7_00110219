#se ide numero de casos
n=int(input("Casos de prueba: "))
i=0     #aterrizaje de contador
i2=0    #aterrizaje de contador secundario
tot=0   #aterrizaje de variable clave
while (i<n):    #ciclo while primario, se repite n veces
    i=i+1   #contador
    
    #se le pide al usuario el rango en el caso i
    a=int(input("inicio de rango "+str(i)+": "))
    b=int(input("fin de rango "+str(i)+": "))
    
    #linea que se ejecuta si el numero de inicio de rango es par
    if (a%2==0):
        a=a+1
        
    #se le asigna el valor de a al contador secundario    
    i2=a
    while (i2<b):   #ciclo que se repite segun la cantidad de numeros impares dentro de un rango i
        i2=i2+2     #contador secundario
        tot=tot+a   #acumulador
        a=a+2       
    i2=0
    print("la suma de los numeros impares en el rango ",i,"es: ",tot)
    tot=0
        
        

