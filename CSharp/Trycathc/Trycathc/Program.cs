using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Trycathc
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("GRRRRRR");
            try// Код который должен будеть работать, и выполнять функцию, а если ошибка,
               // то консоль не вылетит, а исполнит код который находится в блоке Катч
            {
                int a = int.Parse(Console.ReadLine());
                Console.WriteLine("BRRRRRR");
                int b = int.Parse(Console.ReadLine());
                Console.WriteLine($"\n = \n{a + b}");
            }
            catch(FormatException)
            {
                Console.WriteLine("Вы ввели чухню");
            }
            
        }
    }
}
