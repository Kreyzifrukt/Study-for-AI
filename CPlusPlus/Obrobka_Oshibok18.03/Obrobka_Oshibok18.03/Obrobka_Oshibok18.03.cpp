#include <iostream>
#include <string>
using namespace std;

int main()
{
    try
    {
        int a = 10;
        int b;
        cin >> b;

        if (b == 0)
            throw string("division");

        cout << "\nA / b = " << a / b;
    }
    catch (string error)
    {
        if (error == "division")
            cout << "Division by zero";
    }
}