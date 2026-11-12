using ImagesApp_WinF_.Repos;
using ImagesApp.Models;

namespace ImagesApp_WinF_
{
    public partial class Form1 : Form
    {
        private FilesRepo _repo;

        public Form1()
        {
            InitializeComponent();
            _repo = new FilesRepo();

            // 1. Растягиваем изображение на всю ширину и высоту панели без пустых полей
            ViewPanel.SizeMode = PictureBoxSizeMode.StretchImage;

            // 2. Привязываем панель ко всем четырем сторонам окна
            ViewPanel.Dock = DockStyle.Fill;

            // 3. Отправляем картинку на задний план, чтобы она ушла вниз под кнопки и список файлов
            ViewPanel.SendToBack();
        }

        private void OpenBTN_Click(object sender, EventArgs e)
        {
            var dialog = new FolderBrowserDialog();
            if (dialog.ShowDialog() == DialogResult.OK)
            {
                string folderPath = dialog.SelectedPath;
                string[] filePathes = Directory.GetFiles(folderPath);

                FilesList.DataSource = null;
                _repo.FillList(filePathes);

                FilesList.DataSource = _repo.FilesData;
                FilesList.DisplayMember = "FileName";
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void BackBTN_Click(object sender, EventArgs e)
        {
            // Перевіряємо, чи є елементи в репозиторії та чи вибрано якийсь елемент
            if (_repo.FilesData == null || _repo.FilesData.Count == 0) return;

            int currentIndex = FilesList.SelectedIndex;

            // Зменшуємо індекс. Якщо вийшли за початок — переходимо в кінець
            currentIndex--;
            if (currentIndex < 0)
            {
                currentIndex = _repo.FilesData.Count - 1;
            }

            // Перемикаємо виділення v ListBox, це самостійно оновить картинку через FilesList_SelectedIndexChanged
            FilesList.SelectedIndex = currentIndex;
        }

        private void NextBTN_Click(object sender, EventArgs e)
        {
            // Перевіряємо, чи є елементи в репозиторії та чи вибрано якийсь елемент
            if (_repo.FilesData == null || _repo.FilesData.Count == 0) return;

            int currentIndex = FilesList.SelectedIndex;

            // Збільшуємо індекс. Якщо вийшли за кінець — переходимо на початок
            currentIndex++;
            if (currentIndex >= _repo.FilesData.Count)
            {
                currentIndex = 0;
            }

            // Перемикаємо виділення v ListBox, це самостійно оновить картинку через FilesList_SelectedIndexChanged
            FilesList.SelectedIndex = currentIndex;
        }

        private void FilesList_SelectedIndexChanged(object sender, EventArgs e)
        {
            int k = FilesList.SelectedIndex;
            if (k >= 0)
            {
                var item = FilesList.SelectedItem as ImageFile;
                if (item != null && File.Exists(item.FilePath))
                {
                    // Звільняємо стару картинку з пам'яті
                    if (ViewPanel.Image != null)
                    {
                        ViewPanel.Image.Dispose();
                        ViewPanel.Image = null;
                    }

                    // Безпечно завантажуємо зображення через потік
                    using (var stream = new FileStream(item.FilePath, FileMode.Open, FileAccess.Read))
                    {
                        ViewPanel.Image = Image.FromStream(stream);
                    }
                }
            }
        }
    }
}
