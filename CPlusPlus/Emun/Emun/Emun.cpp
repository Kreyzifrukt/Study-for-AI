#include <iostream>
using namespace std;

enum logic {
	plus,
	minus,
	mnozenna,
	division
};

struct calc {
	float a, b;
	logic op;
	void main_logic(){
	switch(op) {
		case logic::plus:
			cout << a << " + " << b << " = " << a + b;
				break;
		case logic::minus:
			cout << a << " - " << b << " = " << a - b;
				break;
		case logic::mnozenna:
			cout << a << " * " << b << " = " << a * b;
				break;
		case logic::division:
			if (b == 0) {
				cout << "\ndivision by zero!" << endl;
			}
			else
				cout << a << " / " << b << " = " << a / b;
					break;
		default:
			cout << "\nWrong choice" << endl;
	}
	}
};

int main() {
	calc c;

	cout << "Enter A and B:\n";
	cin >> c.a >> c.b;

	cout << "Choose operation:\n";
	cout << "0 - plus\n1 - minus\n2 - mnozenna\n3 - division\n";

	int choice;
	cin >> choice;

	c.op = (logic)choice;
	c.main_logic();

}