#include <iostream>
using namespace std;

int main(){
    //solicitud de cantidad de casos
    int n=0;
    cout << "Digite numero de casos "<<endl;cin >> n;
    //processo que se repite segun la cantidad de casos asignados
    for (int i = 1;i<=n;i++){
        
        int a=0;
        int b=0;
        //solicitud de valores
        cout << "Caso " << i << ": "<<endl;
        cout << "Primer numero:"<<endl; cin >> a;
        cout << "Segundo numero:"<<endl; cin >> b;
        //menor
        if (a<b){
            cout << a << " es menor a " << b << endl;
        }
        //mayor
        if (a>b){
            cout << a << " es mayor a " << b << endl;
        }
        //igual
        if (a==b){
            cout << a << " es igual a " << b << endl;
        }

    }
return 0;
}