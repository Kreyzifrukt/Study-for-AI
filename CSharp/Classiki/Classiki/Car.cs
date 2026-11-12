using System;

namespace Classiki
{
    class Car
    {
        private string name;
        private string brand;
        private double weight;
        private int speed;

        public Car(string carName, string carBrand, double carWeight, int carSpeed)
        {
            name = carName;
            brand = carBrand;
            weight = carWeight;
            speed = carSpeed;
        }

        public static void Show_info(Car car)
        {
            Console.WriteLine($"Car name and brand is {car.name + car.brand}\n Car speed is {car.speed}\n Car weight is {car.weight}");
        }

        public void Drive()
        {
            Console.WriteLine($"Car {name} has been moved");
        }
    }
}
