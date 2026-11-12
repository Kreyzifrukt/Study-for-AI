using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HR_App.Models
{
    public class Employee
    {
        public int Id { get; set; }
        public string FullName { get; set; } = string.Empty;
        public int BirthYear { get; set; }
        public string Position { get; set; } = string.Empty;
        public string Category { get; set; } = string.Empty;
        public string Experience { get; set; } = string.Empty;
        public string Phone { get; set; } = string.Empty;
        public string Photo { get; set; } = string.Empty;
        public int DepartmentId { get; set; }

    }
}
