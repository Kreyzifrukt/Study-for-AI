#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    string name;
    int age;
    float awerage;

    void info() {
        cout << "Name - "<< name << "\n Age - " << age << "\nAwerage - " << awerage << endl;
    }
    void isCoolBoy() {
        if (awerage >= 4) {
            cout << "Your`s student has good marks)" << endl;
        }
        else
            cout << "Student has some problem with marks" << endl;
    }

};

int main()
{
    Student s;
    s.name = "Wowa Solodkov";
    s.age = 15;
    s.awerage = 4.1;
    s.isCoolBoy();
    s.info();

}