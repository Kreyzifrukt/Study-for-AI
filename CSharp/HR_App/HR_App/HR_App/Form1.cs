using HR_App.Models;
using HR_App.Services;

namespace HR_App
{
    public partial class DepFieId : Form
    {
        private readonly DepartmentsService _depservice = new();
        private readonly EmployeeService _employee = new();
        private List<Department> _departments = [];
        private int _lastId = 0;
        public DepFieId()
        {
            InitializeComponent();
        }

        private void LoadDepartments()
        {
            _departments.Clear();
            _departments = _depservice.GetAllDepartments();

            int lastIndex = _departments.Count - 1;
            _lastId = _departments[lastIndex].Id;
            DepsCombo.DataSource = _departments;
            DepsCombo.DisplayMember = "Name";

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoadDepartments();
        }

        private void AddDepBtn_Click(object sender, EventArgs e)
        {
            // 1. Прочитаємо назву департаменту
            string depName = DepFieId.Text;

            // 2. Перевіримо чи не є назва порожньою
            if (string.IsNullOrWhiteSpace(depName))
            {
                MessageBox.Show("Ви не вказали назву департаменту", "",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            // 3. перевірка зайтяності імені департаменту...
            //Linq 

            var res = _departments
                .Where(dep => dep.Name == depName)
                .FirstOrDefault();
            // ->
            if (res != null)
            {
                MessageBox.Show("Такий департамент вже існує", "Попередження",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            //4. Додавання департаменту:
            _depservice.AddDepartment(new Department() { Id = _lastId + 1, Name = depName });
            MessageBox.Show("Новий департамент успішно створений!", "Попередження",
                   MessageBoxButtons.OK, MessageBoxIcon.Information);
            DepFieId.Clear();
            LoadDepartments();
        }

        private void DepsCombo_SelectedIndexChanged(object sender, EventArgs e)
        {
            int k = DepsCombo.SelectedIndex;
            if (k > -1)
            {
                var selectedDep = DepsCombo.SelectedItem as Department;
                int depId = selectedDep!.Id;
                EmpsList.DataSource = _empService.getemployeesByDepId(depId);
                EmpsList.DisplayMember = "FillName";
            }
        }

        private void EmpsList_SelectedIndexChanged(object sender, EventArgs e)
        {
            string basePath = @"..\..\..\Images\";
            int k = EmpsList.SelectedIndex;
            if (k > -1)
            {
                var SelEmp = EmpsList.SelectedItem as Employee;
                NameField.Text = SelEmp?.FullName;
                BirthField.Text = SelEmp?.BirthYear.ToString();
                EmailField.Text = SelEmp?.Position;
                ExpField.Text = SelEmp?.Experience;
                PhoneField.Text = SelEmp?.Phone;
                PhotoPanel.Image = Image.FromFile(SelEmp?.Photo);

            }
        }
    }
}
