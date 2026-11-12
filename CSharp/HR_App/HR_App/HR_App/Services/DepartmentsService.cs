using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using HR_App.Models;
using System.IO;

namespace HR_App.Services
{
    public class DepartmentsService
    {
        private readonly string filePath = @"..\..\..\Data\Departments.txt";
        public List<Department> GetAllDepartments()
        {
            var result = new List<Department>();
            string[] rows = File.ReadAllLines(filePath);


            for (int i = 0; i < rows.Length; i += 9)
            {
                int id = Convert.ToInt32(rows[i]);
                string name = rows[i + 1];
                var dep = new Department() { Id = id, Name = name};
                result.Add(dep);
                string position = rows[i + 3];
                string category = rows[i + 4];
                string experience = rows[i + 5];

                string phone = rows[i + 6];
                string photo = rows[i + 7];
                int depId = Convert.ToInt32(rows[i+8]);
                if (departmentId == depId)
                {
                    var emp = new Employee()
                    {
                        Id = id,
                        FullName = name,
                        BirthYear = year,
                        Position = position,
                        Category = category,
                        Experience = experience,
                        Phone = phone,
                        DepartmentId = depId
                    };
                    result.Add(emp);
                }

                }
            public void AddDepartment(Department department)
            {
                string allText = File.ReadAllText(filePath);
                allText += department.Id.ToString();
                allText += "\n" + department.Name + "\n";
            File.WriteAllText(filePath, allText);
            }

            return result;
        }
    }
