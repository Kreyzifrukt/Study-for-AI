#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	ifstream file("dog.txt");
	if (file.is_open()){
		char a[7];
		file.getline(a, 7);
		cout << a << endl;
		file.close();
	}
}