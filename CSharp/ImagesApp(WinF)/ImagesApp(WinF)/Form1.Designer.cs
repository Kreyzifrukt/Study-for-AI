namespace ImagesApp_WinF_
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            groupBox1 = new GroupBox();
            FilesList = new ListBox();
            FolderName = new TextBox();
            OpenBTN = new Button();
            groupBox2 = new GroupBox();
            NextBTN = new Button();
            BackBTN = new Button();
            ViewPanel = new PictureBox();
            groupBox1.SuspendLayout();
            groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)ViewPanel).BeginInit();
            SuspendLayout();
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(FilesList);
            groupBox1.Controls.Add(FolderName);
            groupBox1.Controls.Add(OpenBTN);
            groupBox1.Dock = DockStyle.Left;
            groupBox1.Location = new Point(0, 0);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(200, 450);
            groupBox1.TabIndex = 0;
            groupBox1.TabStop = false;
            groupBox1.Text = "Вибір зображень";
            // 
            // FilesList
            // 
            FilesList.Dock = DockStyle.Fill;
            FilesList.FormattingEnabled = true;
            FilesList.Location = new Point(3, 101);
            FilesList.Name = "FilesList";
            FilesList.Size = new Size(194, 346);
            FilesList.TabIndex = 0;
            FilesList.SelectedIndexChanged += FilesList_SelectedIndexChanged;
            // 
            // FolderName
            // 
            FolderName.Dock = DockStyle.Top;
            FolderName.Location = new Point(3, 78);
            FolderName.Name = "FolderName";
            FolderName.ReadOnly = true;
            FolderName.Size = new Size(194, 23);
            FolderName.TabIndex = 0;
            FolderName.TextAlign = HorizontalAlignment.Center;
            // 
            // OpenBTN
            // 
            OpenBTN.Dock = DockStyle.Top;
            OpenBTN.Location = new Point(3, 19);
            OpenBTN.Name = "OpenBTN";
            OpenBTN.Size = new Size(194, 59);
            OpenBTN.TabIndex = 0;
            OpenBTN.Text = "Відкрити папку";
            OpenBTN.UseVisualStyleBackColor = true;
            OpenBTN.Click += OpenBTN_Click;
            // 
            // groupBox2
            // 
            groupBox2.Controls.Add(NextBTN);
            groupBox2.Controls.Add(BackBTN);
            groupBox2.Controls.Add(ViewPanel);
            groupBox2.Dock = DockStyle.Top;
            groupBox2.Location = new Point(200, 0);
            groupBox2.Name = "groupBox2";
            groupBox2.Size = new Size(600, 450);
            groupBox2.TabIndex = 1;
            groupBox2.TabStop = false;
            groupBox2.Text = "Перегляд зображень";
            // 
            // NextBTN
            // 
            NextBTN.Location = new Point(291, 0);
            NextBTN.Name = "NextBTN";
            NextBTN.Size = new Size(144, 45);
            NextBTN.TabIndex = 5;
            NextBTN.Text = "Вперед";
            NextBTN.UseVisualStyleBackColor = true;
            NextBTN.Click += NextBTN_Click;
            // 
            // BackBTN
            // 
            BackBTN.Location = new Point(153, 0);
            BackBTN.Name = "BackBTN";
            BackBTN.Size = new Size(123, 45);
            BackBTN.TabIndex = 4;
            BackBTN.Text = "Назад";
            BackBTN.UseVisualStyleBackColor = true;
            BackBTN.Click += BackBTN_Click;
            // 
            // ViewPanel
            // 
            ViewPanel.Dock = DockStyle.Fill;
            ViewPanel.Location = new Point(3, 19);
            ViewPanel.Name = "ViewPanel";
            ViewPanel.Size = new Size(594, 428);
            ViewPanel.TabIndex = 3;
            ViewPanel.TabStop = false;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(groupBox2);
            Controls.Add(groupBox1);
            Name = "Form1";
            Text = "Менеджер зображень";
            WindowState = FormWindowState.Maximized;
            Load += Form1_Load;
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            groupBox2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)ViewPanel).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private GroupBox groupBox1;
        private Button OpenBTN;
        private GroupBox groupBox2;
        private ListBox FilesList;
        private TextBox FolderName;
        private PictureBox ViewPanel;
        private Button NextBTN;
        private Button BackBTN;
    }
}
