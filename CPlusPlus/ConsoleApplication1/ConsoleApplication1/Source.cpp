#include <iostream>
#include <ctime>
using namespace std;

int main() {
	setlocale(LC_ALL, "Uk-ua");
	cout << "This is elevator logic program" <<endl;
	int a, b;
	srand(time(NULL));
	a = rand();
	b = rand();

	if (a > b) {
		cout << "Elevator a is nearly then b, a is run to you";
	}
	else if (b > a) {
		cout << "Elevator b is nearly then a, a is run to you";
	}
	else {
		cout << "We choose random Elevator";

	}

	return 0;
}