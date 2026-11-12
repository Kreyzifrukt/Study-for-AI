#include <iostream>
#include <string>
using namespace std;

struct farm {
	string name;
	int number;
	float years;
	int owner;
	float quality;

	void get_info() {
		cout << "Name = " << name << "\nNumber = " << number << "\nYears = " << years << "\nOwners = " << owner << "\nQuality = " << quality << endl;
	}
};

int main()
{
	farm edelveys;
	edelveys.name = "Rancho";
	edelveys.number = 1;
	edelveys.years = 1342;
	edelveys.owner = 3;
	edelveys.quality = 4.5;
	edelveys.get_info();
}
