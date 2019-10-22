#include <iostream>
#include <stdlib.h>
using namespace std;
//Funcion que encuentra si un numero es primo o no 
int primus (int x){
    int i = 1;
    int sob = 0;
    while(i<x-1){
        i=i+1;
        sob=x%i;
        if (sob==0){
            return 0;
        }
        if (i==x-1){
            return x;
        }
    }
}
// funcion principal
int main(){
    int x=0,y=0,ret=0;
    cout << "digite inicio de rango: "; cin >> x;
    cout << endl;
    cout << "digite final de rango: "; cin >> y;
    cout << endl;
    int aux = x - 1;
//ciclo en donde se examina que un numero dentro del rango no sea divisible mas que por 1 y el mismo
    while(aux<y){
        salto:
        aux=aux+1;
        ret=primus(aux);
        //parametro de salida para una sola linea
        if (aux==x){
            cout << "los numeros primos en el rango indicado son " << endl;
        }
        //parametro que borra los return de 0 de el resultado final
        if (ret==0){
            goto salto;
        }
        //parametro que elimina un error de conteo donde muestra un numero primo mayor al del final de rango
        if (ret > y){
            return 0;
        }
        cout << ret;
        cout << ", ";
    }
    return 0;
}

