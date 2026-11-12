using HR_App.Models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HR_App.Services
{
    internal class EmployeeService
    {
        private readonly string filePath = @"..\..\..\Data\Employee.txt";

        public List<Employee> GetEmployeesByDepId(int departmentId)
        {
            var result = new List<Employee>();
            string[] rows = File.ReadAllLines(filePath);

            for (int i = 0; i < rows.Length; i += 8)
            {
                int id = Convert.ToInt32(rows[i]);
                string name = rows[i + 1];
                int year = Convert.ToInt32(rows[i + 2]);
                string position = rows[i + 3];

                string experience = rows[i + 4];
                string phone = rows[i + 5];
                string photo = rows[i + 6];
                int depId = Convert.ToInt32(rows[i + 7]);

                if (departmentId == depId)
                {
                    var emp = new Employee()
                    {
                        Id = id,
                        FullName = name,
                        Year = year,
                        Position = position,
                        Experience = experience,
                        Phone = phone,
                        Photo = photo,
                        DepartmentId = depId
                    };

                    result.Add(emp);
                }
            }

            return result;
        }
    }
}
