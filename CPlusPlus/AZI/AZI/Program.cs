using System;

namespace Sproba
{
    class Barabulka
    {
        static void Main()
        {
            Console.WriteLine("Привет, это калькулятор на С#\nВведи первое число");
            int number1 = Convert.ToByte(Console.ReadLine());
            
            Console.WriteLine("Введи 2 число");
            int number2 = Convert.ToByte(Console.ReadLine());
            
            Console.WriteLine("Введи Операцию которую ты хочешь (+ - / *)");
            char op = Convert.ToChar(Console.ReadLine());
            if (op == '+') 
            {
                Console.WriteLine(number1 + number2);
            }
            else if (op == '-') 
            {
                Console.WriteLine(number1 - number2);
            }
            else if (op == '*') 
            {
                Console.WriteLine(number1 * number2);
            }
            else if (op == '/') 
            {
                Console.WriteLine(number1 / number2);
            }
            else
            {
                Console.WriteLine("Wrong Choice :(");
            }
        }
    }
}