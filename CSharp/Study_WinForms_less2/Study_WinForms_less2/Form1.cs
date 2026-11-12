using System.Diagnostics;

namespace Study_WinForms_less2
{
    public partial class Form1 : Form
    {
        private string alarm = "";
        private string current = "";

        public Form1()
        {
            InitializeComponent();
            DisplayTime();
        }

        private void DisplayTime()
        {
            current = DateTime.Now.ToLongTimeString();
            label1.Text = current;
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Enabled = false;
            button2.Enabled = true;
            string alarmText = textBox1.Text;

            if (string.IsNullOrWhiteSpace(alarmText))
            {
                MessageBox.Show("Дані про встановлення будильника відсутні",
                    "Попередження", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                alarm = alarmText;

                MessageBox.Show($"Будильник встановленний на {alarm}",
                    "Повідомлення", MessageBoxButtons.OK, MessageBoxIcon.Information);

                textBox1.ReadOnly = true;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            button1.Enabled = true;
            button2.Enabled = false;

            alarm = "00:00:00";
            textBox1.Text = alarm;

            //Таймер

            label2.Text = "00:00:00";

            //Таймер

            MessageBox.Show($"Будильник вимкненний",
                "Повідомлення", MessageBoxButtons.OK, MessageBoxIcon.Information);

            textBox1.ReadOnly = false;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            DisplayTime();

            //Таймер

            if (TimeSpan.TryParse(alarm, out TimeSpan alarmTime))
            {
                TimeSpan currentTime = DateTime.Now.TimeOfDay;
                TimeSpan remaining = alarmTime - currentTime;

                if (remaining.TotalSeconds < 0)
                {
                    remaining = remaining.Add(TimeSpan.FromDays(1));
                }

                label2.Text = remaining.ToString(@"hh\:mm\:ss");
            }

            //Таймер

            if (current == alarm)
            {
                //string file = @"..\..\..\Music\melody.mp3";
                MessageBox.Show("Заданий час настав!", "Повідомлення",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);

                Process.Start(new ProcessStartInfo()
                {
                    //FileName = file
                });
            }
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
}
