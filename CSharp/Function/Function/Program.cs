using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Function
{
    internal class Program
    {
        static float average(int[] byba)
        {
            int sum = 0;
            for (int i = 0; i < byba.Length; i++)
            {
                sum += byba[i];
            }
            return (float)sum / byba.Length;
        }
        static void Main()
        {
            int[] numbers = { 5, 6, 7, 8, 9,11,32 }; 
            Console.WriteLine(average(numbers));
        }
    }
}
