#include <iostream>
using namespace std;
int main()
    {
        char name[30];
        cout << "may i have your name and phone number?" << endl;
       // cin >> name; /* cin은 공백/띄어쓰기를 입력받지 못함.*/
        cin.getline(name, sizeof(name));
        int Total_price, point;
        cout << "please key in your price" << endl;
        cin >> Total_price;
        point = Total_price*0.01 ; 
        cout << "hello " << name << ", your point is " << point << " won\n" ;
    }