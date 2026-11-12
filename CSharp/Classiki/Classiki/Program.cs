using System;
namespace Classiki
{
    internal class Program
    {
        static void Main()
        {
            Car car1 = new Car("Camry", "Toyota", 1500, 180);
            Car car2 = new Car("M5", "BMW", 1900, 250);

            // Вызываем методы
            car1.Drive();
            car2.Drive();

            Console.WriteLine("\n--- Информация ---");
            Car.Show_info(car1);
        }
    }
}
