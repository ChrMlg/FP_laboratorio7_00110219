#include <iostream>
using namespace std;

int main(){
    int tot=0;
    int n=0;
    cout << "Numero de casos de prueba: " << endl;
    cin >> n;
   //procedimiento que se repita segun el numero de casos que se especifique
    for(int i=1;i<=n;i++){
        //reinicializacion de valores 
        int a=0;
        int b=0;
        //solicitud de valores
        cout << "Caso "<<i<<" :"<<endl;
        cout << "Inicio de rango "<<i<<" :"; cin >> a;
        cout << "" << endl;
        cout << "Final de rango "<<i<<" :"; cin >> b;
        cout << "" << endl;
        //parametro que convierte el numero a impar en el caso de que el primer numero sea par
        if (a%2==0){
            a=a+1;
        }
        //ciclo de acumuladores 
        for (int j = a; j<b; j=j+2){
            tot=tot+a;
            a=a+2;
        }

        cout<<tot<<endl;
        
        tot=0;
    }
return 0;
}